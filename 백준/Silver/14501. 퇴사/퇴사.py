import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
for i in range(N):
    T, P = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])
    if i+T <= N:
        dp[i+T] = max(dp[i+T], dp[i]+P)

print(max(dp))