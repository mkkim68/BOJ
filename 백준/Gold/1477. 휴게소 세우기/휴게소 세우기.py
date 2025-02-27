import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rests = [0] + sorted(list(map(int ,input().split()))) + [L]

s, e = 1, L-1
ans = 0
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in range(1, len(rests)):
        if rests[i] - rests[i-1] > m:
            cnt += (rests[i] - rests[i-1] - 1) // m

    if cnt > M:
        s = m + 1
    else:
        ans = m
        e = m - 1

print(ans)