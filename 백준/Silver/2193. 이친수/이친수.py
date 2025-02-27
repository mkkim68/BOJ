import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1, 1, 2, 3]

for i in range(5, N+1):
    dp.append(dp[i-2] + dp[i-1])

print(dp[N])