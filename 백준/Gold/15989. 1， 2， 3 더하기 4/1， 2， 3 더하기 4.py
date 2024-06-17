import sys
input = sys.stdin.readline


def sol(n):
    dp = [0, 1, 2, 3, 4, 5]
    if n <= 5:
        return dp[n]
    for i in range(6, n+1):
        a = i//2 + 1 + dp[i-3]
        dp.append(a)
    return dp


T = int(input())

nums = []
for tc in range(T):
    N = int(input())
    nums.append(N)

m = max(nums)
dp = sol(m)

for tc in range(T):
    print(dp[nums[tc]])