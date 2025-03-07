import sys
input = sys.stdin.readline

N = int(input())
N //= 2
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j] % 987654321

    dp[i] %= 987654321

print(dp[N])