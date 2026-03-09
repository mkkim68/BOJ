import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))
times.sort()

s, e = 1, times[-1] * M
ans = 1000000000001
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for t in times:
        cnt += m // t

    if cnt >= M:
        ans = min(ans, m)
        e = m - 1
    else:
        s = m + 1

print(ans)