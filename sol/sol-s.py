import asyncio
import websockets
import json
from datetime import datetime
from solana.rpc.api import Client
from solders.signature import Signature

RPC_URL = "wss://api.mainnet-beta.solana.com"

# 目标地址
TARGET_ADDRESS = "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"

# 常见 swap 程序 ID
SWAP_PROGRAM_IDS = {
    "Serum": "9xQeWvG816bUx9EPZ96kxvF9Kb7nYjrrjMJZBPg5bQP",
    "Raydium": "EhhTKt74FJUMDHFZHRaBLZbU1Sh4XG8BUH5kE5cEfJxz",
    'r': '675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8',
}


async def send_heartbeat(websocket):
    """
    定期发送心跳消息，保持连接
    """
    while True:
        await asyncio.sleep(30)  # 每 30 秒发送一次心跳
        try:
            await websocket.send(json.dumps({"jsonrpc": "2.0", "method": "ping"}))
            print("Heartbeat sent")
        except Exception as e:
            print("Failed to send heartbeat:", e)
            break


async def subscribe_logs():
    """
    订阅日志，并定期发送心跳保持连接
    """
    while True:  # 如果连接断开，尝试重连
        try:
            async with websockets.connect(RPC_URL) as websocket:
                # 构造订阅请求
                request = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "logsSubscribe",
                    "params": [{"mentions": [TARGET_ADDRESS]}]
                }
                await websocket.send(json.dumps(request))
                print(f"Subscribed to logs for address: {TARGET_ADDRESS}")

                # 启动心跳任务
                heartbeat_task = asyncio.create_task(send_heartbeat(websocket))

                # 接收日志数据
                while True:
                    response = await websocket.recv()
                    data = json.loads(response)

                    # 处理日志
                    if "params" in data:
                        log = data["params"]["result"]
                        await process_log(log)
        except websockets.ConnectionClosed:
            print("Connection closed, reconnecting...")
            await asyncio.sleep(5)  # 连接关闭后稍等再尝试重连
        except Exception as e:
            print(f"Unexpected error: {e}, reconnecting...")
            await asyncio.sleep(5)  # 出现其他异常时，等待后重连


async def process_log(log):
    """
    处理日志数据
    """
    print("New Log Received:", log)
    # 将日志保存到本地
    await save_log_to_file(log)
    signature = log['value']['signature']
    await fetch_transaction_details(signature)



async def save_log_to_file(log):
    """
    将日志保存到本地文件
    """
    try:
        # 获取当前时间，作为日志文件的一部分
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "log": log
        }

        # 保存日志到文本文件
        with open("solana_logs.txt", "a") as file:
            file.write(json.dumps(log_entry, indent=4))
            file.write("\n\n")  # 每条日志之间添加空行

        print("Log saved to solana_logs.txt")
    except Exception as e:
        print(f"Error saving log: {e}")


async def fetch_transaction_details(signature):
    """
    获取并解析交易详情
    """
    print(signature)
    async with websockets.connect(RPC_URL) as websocket:
        # 请求交易详情
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTransaction",
            "params": [signature, {"encoding": "json"}]
        }
        await websocket.send(json.dumps(request))
        response = await websocket.recv()
        data = json.loads(response)
        print(data)
        # print(data['value'])
        # await analyze_transaction(data["result"])


async def analyze_transaction(signature):
    print("Analyzing transaction：" + signature)
    """
    解析交易内容，提取金额和方向
    """
    solana_client = Client(
        "https://dawn-white-spree.solana-mainnet.quiknode.pro/b3e9230f3aa92d09ffd82a467ec08c8b2cea750a/")

    # 使用签名字符串获取交易
    sig = Signature.from_string(signature)

    # 获取交易信息
    response = solana_client.get_transaction(sig, encoding="jsonParsed", max_supported_transaction_version=0)
    data = json.loads(response.to_json())
    contract = ''
    new_transaction = False
    # 检查是否有特定的 programId
    instructions = data["result"]["transaction"]["message"]["instructions"]
    for instruction in instructions:
        if instruction.get("programId") == "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8":
            print("发现新的交易")
            new_transaction = True
            break
    if new_transaction:
        # 分析 preTokenBalances 和 postTokenBalances
        pre_balances = data["result"]["meta"].get("preTokenBalances", [])
        post_balances = data["result"]["meta"].get("postTokenBalances", [])

        pre_amount = 0
        post_amount = 0
        for item in pre_balances:
            if item.get("owner") == TARGET_ADDRESS:
                pre_amount = float(item["uiTokenAmount"]["uiAmountString"])
                break

        for item in post_balances:
            if item.get("owner") == TARGET_ADDRESS:
                contract = item.get("mint")
                post_amount = float(item["uiTokenAmount"]["uiAmountString"])
                break

        # 判断买入或卖出
        if pre_amount is None and post_amount is not None:
            print("买入：" + contract)
        elif pre_amount is not None and post_amount is not None and pre_amount < post_amount:
            print("买入：" + contract)
        elif pre_amount is not None and post_amount is not None and pre_amount > post_amount:
            print("卖出：" + contract)
        else:
            print("未发生买入或卖出")
    else:
        print('未有新的交易')

# 启动任务
asyncio.run(subscribe_logs())
