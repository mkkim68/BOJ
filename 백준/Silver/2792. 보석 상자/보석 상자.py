import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jewels = list(int(input()) for _ in range(M))

def check(num):
    cnt = 0
    for now in jewels:
        if now % num:
            cnt += now // num + 1
        else:
            cnt += now // num
    if cnt <= N:
        return True
    return False

T = sum(jewels)
ans = T
s, e = 1, T
while s <= e:
    m = (s+e) // 2
    if check(m):
        ans = min(ans, m)
        e = m - 1
    else:
        s = m + 1

print(ans)
