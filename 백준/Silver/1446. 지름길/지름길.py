import sys
input = sys.stdin.readline

N, D = map(int, input().split())
dp = [i for i in range(D+1)]
edge = {}
for _ in range(N):
    s, e, w = map(int, input().split())
    if e in edge:
        edge[e].append([s, w])
    else:
        edge[e] = [[s, w]]

for i in range(D+1):
    if i in edge:
        for s, w in edge[i]:
            try:
                dp[i] = min(dp[i], dp[s] + w, dp[i - 1] + 1)
            except:
                pass
    dp[i] = min(dp[i], dp[i - 1] + 1)

# for i in range(D+1):
#     print(i,':', dp[i])

print(dp[D])