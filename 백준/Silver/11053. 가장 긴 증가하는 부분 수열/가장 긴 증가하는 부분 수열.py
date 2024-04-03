import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    cur = A[i]
    for j in range(0, i):
        prev = A[j]
        if prev < cur:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
