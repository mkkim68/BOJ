import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = set(arr)

pages = []
for i in range(1, N+1):
    if i not in arr:
        pages.append(i)

dp = [0] * len(pages)
for i in range(len(pages)):
    if i > 0:
        dp[i] = min(7+dp[i-1], dp[i-1] + 2 * (pages[i]-pages[i-1]))
    else:
        dp[i] = 7
if dp:
    print(dp[-1])
else:
    print(0)