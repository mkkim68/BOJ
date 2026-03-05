import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

prefix_sum = [0] * (N+1)
prefix_sum[1] = arr[0]
for i in range(2, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]


dp = [[0] * (N+1) for _ in range(4)]


for i in range(1, 4):
    for j in range(i*M, N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + prefix_sum[j] - prefix_sum[j-M])

print(dp[-1][-1])