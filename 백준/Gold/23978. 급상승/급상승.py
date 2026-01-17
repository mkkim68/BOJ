import sys
input = sys.stdin.readline

def chk(X):
    cnt = 0
    for i in range(N-1):
        n, t = dates[i], dates[i+1]
        if X > t-n:
            cnt += (X + X-(t-n)+1) * ((t-n) // 2) + (X-(t-n)//2) * ((t-n) % 2)
        else:
            cnt += X * (X + 1) // 2
    cnt += X * (X+1) // 2
    if cnt >= K:
        return cnt
    return False

N, K = map(int, input().split())
dates = list(map(int, input().split()))

X = K+1
s, e = 1, K+1
while s <= e:
    m = (s+e) // 2
    temp = chk(m)

    if temp:
        X = min(X, m)
        e = m - 1
    else:
        s = m + 1

print(X)