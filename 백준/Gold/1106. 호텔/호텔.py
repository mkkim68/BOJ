import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 비용, 고객 수

L = C + max(cus for _, cus in arr) + 100
dp = [1e9] * L
dp[0] = 0
for cost, customer in arr:
    for i in range(1, L):
        dp[i] = min(dp[i], dp[i-customer] + cost)

print(min(dp[C:]))