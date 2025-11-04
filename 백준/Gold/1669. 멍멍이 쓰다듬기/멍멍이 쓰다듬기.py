import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
dif = Y - X

cnt = 0
now = 1
while dif > 0:
    dif -= now
    cnt += 1

    if dif <= 0:
        break

    dif -= now
    cnt += 1
    now += 1

print(cnt)