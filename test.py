import pyupbit
access = "ve3i2WteSv4rNnlXLVbPqxWTALnSqbqOXgsu2N8j"          # 본인 값으로 변경
secret = "YfaGMtv9IU8kefuc9gADDIbT3kXUiFu8dVR6xqel"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
