import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
last = 0
max_dis = 0
distances = []
for i in range(M):
    now = int(input())
    dis = now-last-1
    if dis > 0:
        distances.append(dis)
        max_dis = max(max_dis, dis)
    last = now

if N-last > 0:
    distances.append(N-last)
    max_dis = max(max_dis, N-last)

dp = [0, 1, 2] + [0] * (max_dis-2)
for i in range(3, max_dis+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
for dis in distances:
    ans *= dp[dis]

print(ans)