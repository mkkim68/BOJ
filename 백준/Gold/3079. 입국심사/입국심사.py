import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
times.sort()

def check(time):
    cnt = 0
    for t in times:
        cnt += time // t
    return cnt

s, e = 0, times[-1] * M
answer = 0
while s <= e:
    m = (s + e) // 2
    cnt = check(m)
    if M <= cnt:
        answer = m
        e = m - 1
    else:
        s = m + 1


print(answer)