import sys

dp = [0] * 11

dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2
dp[3] = 4  # 1+1+1, 1+2, 2+1, 3

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

input_data = sys.stdin.read().split()

if input_data:
    t = int(input_data[0]) 
    for i in range(1, t + 1):
        n = int(input_data[i])
        print(dp[n])