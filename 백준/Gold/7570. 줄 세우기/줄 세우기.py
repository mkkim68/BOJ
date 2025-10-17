import sys
input = sys.stdin.readline

N = int(input())
children = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(N):
    idx = children[i]
    dp[idx] = dp[idx-1] + 1

print(N - max(dp))