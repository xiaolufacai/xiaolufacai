from solana.rpc.api import Client
from solders.signature import Signature

# Solana 客户端设置
solana_client = Client("https://dawn-white-spree.solana-mainnet.quiknode.pro/b3e9230f3aa92d09ffd82a467ec08c8b2cea750a/")

# 使用签名字符串获取交易
sig = Signature.from_string("3tsTccv25b1G7uRX2XnatT2WqrR8ghhWWmymie6xPTfAgwYbEJR5VHNFAtqu7PRRH64ZsHzMi8HDwB77WSy6RJNJ")

# 获取交易信息
response = solana_client.get_transaction(sig, encoding="jsonParsed", max_supported_transaction_version=0)

# 打印响应类型
# print(type(response))

# 打印响应的内容，查看其中的数据
# print(response)
# 打印所有属性和方法
# print(dir(response))

# 获取响应数据，通常它会在 result 或 data 中
print(response.to_json())  # 或者尝试其他属性如 response.data
