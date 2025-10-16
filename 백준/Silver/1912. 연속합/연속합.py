import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
for i in range(1, N):
    temp = max(dp[i-1]+arr[i], arr[i])
    dp.append(temp)

print(max(dp))