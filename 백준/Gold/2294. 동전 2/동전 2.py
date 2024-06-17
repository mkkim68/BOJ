import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))

dp = [int(1e9)] * (K+1)
coins = sorted(list(set(coins)), reverse=True)

for c in coins:
    if c <= K:
        dp[c] = 1
    for idx in range(K):
        if dp[idx] < 1e9:
            try:
                dp[idx+c] = min(dp[idx+c], dp[idx]+1)
            except:
                break
    i = 2
    while i * c <= K:
        dp[i*c] = min(dp[(i-1)*c]+1, dp[i*c])
        i += 1


if dp[K] < 1e9:
    print(dp[K])
else:
    print(-1)