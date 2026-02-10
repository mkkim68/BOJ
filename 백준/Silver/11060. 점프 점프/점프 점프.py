import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1e9] * N
dp[0] = 0
for i in range(N):
    now = arr[i]
    for j in range(i+1, min(N, i+now+1)):
        dp[j] = min(dp[j], dp[i] + 1)

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])
