import json

# 示例 JSON 数据 (将实际数据替换到这里)
target_owner = "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
jsons = '''{
    "jsonrpc": "2.0",
    "result": {
        "slot": 303059653,
        "transaction": {
            "signatures": [
                "qBABeme8J8o7z1BWffPDaeDiYn9aF2R8Qs7aKVds6NFfNrTMmK3Up2J5GqiArVow31Uy33NNa5QGvCBw9HLNzRa"
            ],
            "message": {
                "accountKeys": [
                    {
                        "pubkey": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                        "writable": true,
                        "signer": true
                    },
                    {
                        "pubkey": "AqvWkY135BYtNyw2bftGnScWyYMdim8BVhoKrVDf9D6X",
                        "writable": true,
                        "signer": false
                    }
                ],
                "recentBlockhash": "EE3B2zrywShzcZEiHDjmUTwBWjSV3hRHkJZXBiGgj7L",
                "instructions": [
                    {
                        "programId": "tro46jTMkb56A3wPepo5HT7JcvX9wFWvR8VaJzgdjEf",
                        "accounts": [
                            "AqvWkY135BYtNyw2bftGnScWyYMdim8BVhoKrVDf9D6X",
                            "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                            "SysvarRent111111111111111111111111111111111",
                            "11111111111111111111111111111111"
                        ],
                        "data": "cmGPJQeeMnKpkRwPi34hjHnXx6b"
                    },
                    {
                        "program": "system",
                        "programId": "11111111111111111111111111111111",
                        "parsed": {
                            "info": {
                                "base": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                                "lamports": 2039280,
                                "newAccount": "7piXtLodyY7njk7eWqgt1jh8ux7dWjkmTKRwW2nEED1k",
                                "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                                "seed": "77E91L6GPissU9SJQJtHdHEERLsfLnVn",
                                "source": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                                "space": 165
                            },
                            "type": "createAccountWithSeed"
                        }
                    },
                    {
                        "program": "spl-token",
                        "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                        "parsed": {
                            "info": {
                                "account": "7piXtLodyY7njk7eWqgt1jh8ux7dWjkmTKRwW2nEED1k",
                                "mint": "So11111111111111111111111111111111111111112",
                                "owner": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                                "rentSysvar": "SysvarRent111111111111111111111111111111111"
                            },
                            "type": "initializeAccount"
                        }
                    },
                    {
                        "programId": "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",
                        "accounts": [
                            "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                            "59Yh916Q31kmGhXTcTsSRfaNrrYoSBTTV3yUkQBpnSWm",
                            "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                            "7piXtLodyY7njk7eWqgt1jh8ux7dWjkmTKRwW2nEED1k",
                            "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
                        ],
                        "data": "6ENUPnQ4UtumQFgQjL7XHyZ"
                    },
                    {
                        "program": "spl-token",
                        "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                        "parsed": {
                            "info": {
                                "account": "7piXtLodyY7njk7eWqgt1jh8ux7dWjkmTKRwW2nEED1k",
                                "destination": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                                "owner": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
                            },
                            "type": "closeAccount"
                        }
                    },
                    {
                        "program": "system",
                        "programId": "11111111111111111111111111111111",
                        "parsed": {
                            "info": {
                                "destination": "9yMwSPk9mrXSN7yDHUuZurAh1sjbJsfpUqjZ7SvVtdco",
                                "lamports": 72832021,
                                "source": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
                            },
                            "type": "transfer"
                        }
                    }
                ],
                "addressTableLookups": [
                    {
                        "accountKey": "2immgwYNHBbyVQKVGCEkgWpi53bLwWNRMB5G2nbgYV17",
                        "writableIndexes": [

                        ],
                        "readonlyIndexes": [
                            5,
                            11
                        ]
                    }
                ]
            }
        },
        "meta": {
            "err": null,
            "status": {
                "Ok": null
            },
            "fee": 25005001,
            "preBalances": [
                3238533190049,
                981360
            ],
            "postBalances": [
                3246414112073,
                981360
            ],
            "innerInstructions": [
                {
                    "index": 5,
                    "instructions": [
                        {
                            "program": "spl-token",
                            "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                            "parsed": {
                                "info": {
                                    "amount": "436920893592",
                                    "authority": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                                    "destination": "B3r7pmWAmoRGA9xAWS7Qh2UbNeHvxxSQiFpwXzZ49ECj",
                                    "source": "mKQsSdT5XsGs4CLLbyjnLGUqrqqh6DftfAMTmx2vFSo"
                                },
                                "type": "transfer"
                            }
                        },
                        {
                            "program": "spl-token",
                            "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                            "parsed": {
                                "info": {
                                    "amount": "7978759046",
                                    "authority": "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                                    "destination": "7piXtLodyY7njk7eWqgt1jh8ux7dWjkmTKRwW2nEED1k",
                                    "source": "8QjhioAmeTdqcJXge63YJLyjPQdfM8uZYPc6GLQ4XGYx"
                                },
                                "type": "transfer"
                            }
                        }
                    ]
                }
            ],
            "logMessages": [
                "Program ComputeBudget111111111111111111111111111111 invoke [1]",
                "Program ComputeBudget111111111111111111111111111111 success",
                "Program ComputeBudget111111111111111111111111111111 invoke [1]",
                "Program ComputeBudget111111111111111111111111111111 success",
                "Program tro46jTMkb56A3wPepo5HT7JcvX9wFWvR8VaJzgdjEf invoke [1]",
                "Program log: Instruction: IncrementNonceAndTimeoutCheck",
                "Program log: Current Timestamp: 1732333691000",
                "Program log: Max Timestamp: 1732333771506",
                "Program tro46jTMkb56A3wPepo5HT7JcvX9wFWvR8VaJzgdjEf consumed 9052 of 419700 compute units",
                "Program tro46jTMkb56A3wPepo5HT7JcvX9wFWvR8VaJzgdjEf success",
                "Program 11111111111111111111111111111111 invoke [1]",
                "Program 11111111111111111111111111111111 success",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [1]",
                "Program log: Instruction: InitializeAccount",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 3443 of 410498 compute units",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
                "Program 675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8 invoke [1]",
                "Program log: ray_log: A5jAg7plAAAAXcz+mQEAAAABAAAAAAAAAPaFJUn5AwAARTazhpwAAADDLLqMACEAAIYzktsBAAAA",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]",
                "Program log: Instruction: Transfer",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4645 of 388065 compute units",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]",
                "Program log: Instruction: Transfer",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4736 of 380439 compute units",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
                "Program 675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8 consumed 32429 of 407055 compute units",
                "Program 675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8 success",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [1]",
                "Program log: Instruction: CloseAccount",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 2915 of 374626 compute units",
                "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
                "Program 11111111111111111111111111111111 invoke [1]",
                "Program 11111111111111111111111111111111 success"
            ],
            "preTokenBalances": [
                {
                    "accountIndex": 6,
                    "mint": "So11111111111111111111111111111111111111112",
                    "uiTokenAmount": {
                        "uiAmount": 672.274789957,
                        "decimals": 9,
                        "amount": "672274789957",
                        "uiAmountString": "672.274789957"
                    },
                    "owner": "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 7,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": 36286244.728003,
                        "decimals": 6,
                        "amount": "36286244728003",
                        "uiAmountString": "36286244.728003"
                    },
                    "owner": "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 12,
                    "mint": "So11111111111111111111111111111111111111112",
                    "uiTokenAmount": {
                        "uiAmount": null,
                        "decimals": 9,
                        "amount": "0",
                        "uiAmountString": "0"
                    },
                    "owner": "G8FMvUa4CAautQdkXt4TXtouLKvg7P3ZtQ6PyeiB6UYW",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 13,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": null,
                        "decimals": 6,
                        "amount": "0",
                        "uiAmountString": "0"
                    },
                    "owner": "G8FMvUa4CAautQdkXt4TXtouLKvg7P3ZtQ6PyeiB6UYW",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 14,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": 4369208.935926,
                        "decimals": 6,
                        "amount": "4369208935926",
                        "uiAmountString": "4369208.935926"
                    },
                    "owner": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                }
            ],
            "postTokenBalances": [
                {
                    "accountIndex": 6,
                    "mint": "So11111111111111111111111111111111111111112",
                    "uiTokenAmount": {
                        "uiAmount": 664.296030911,
                        "decimals": 9,
                        "amount": "664296030911",
                        "uiAmountString": "664.296030911"
                    },
                    "owner": "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 7,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": 36723165.621595,
                        "decimals": 6,
                        "amount": "36723165621595",
                        "uiAmountString": "36723165.621595"
                    },
                    "owner": "5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 12,
                    "mint": "So11111111111111111111111111111111111111112",
                    "uiTokenAmount": {
                        "uiAmount": null,
                        "decimals": 9,
                        "amount": "0",
                        "uiAmountString": "0"
                    },
                    "owner": "G8FMvUa4CAautQdkXt4TXtouLKvg7P3ZtQ6PyeiB6UYW",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 13,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": null,
                        "decimals": 6,
                        "amount": "0",
                        "uiAmountString": "0"
                    },
                    "owner": "G8FMvUa4CAautQdkXt4TXtouLKvg7P3ZtQ6PyeiB6UYW",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                },
                {
                    "accountIndex": 14,
                    "mint": "45A2W6WEkQGkLpawnkkDhgNMKkTs3oYHrabxfUzppump",
                    "uiTokenAmount": {
                        "uiAmount": 3932288.042334,
                        "decimals": 6,
                        "amount": "3932288042334",
                        "uiAmountString": "3932288.042334"
                    },
                    "owner": "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm",
                    "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
                }
            ],
            "rewards": [

            ]
        },
        "version": 0,
        "blockTime": 1732333691
    },
    "id": 0
}
'''

data = json.loads(jsons)
print(data)
contract = ''
# 检查是否有特定的 programId
instructions = data["result"]["transaction"]["message"]["instructions"]
for instruction in instructions:
    if instruction.get("programId") == "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8":
        print("发现新的交易")
        break

# 分析 preTokenBalances 和 postTokenBalances
pre_balances = data["result"]["meta"].get("preTokenBalances", [])
post_balances = data["result"]["meta"].get("postTokenBalances", [])

pre_amount = 0
post_amount = 0
for item in pre_balances:
    if item.get("owner") == target_owner:
        pre_amount = item["uiTokenAmount"]["uiAmountString"]
        break

for item in post_balances:
    if item.get("owner") == target_owner:
        contract = item.get("mint")
        post_amount = item["uiTokenAmount"]["uiAmountString"]
        break

# 判断买入或卖出
if pre_amount is None and post_amount is not None:
    print("买入："+contract)
elif pre_amount is not None and post_amount is not None and pre_amount < post_amount:
    print("买入："+contract)
elif pre_amount is not None and post_amount is not None and pre_amount > post_amount:
    print("卖出："+contract)
else:
    print("未发生买入或卖出")
