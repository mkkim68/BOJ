import sys
input = sys.stdin.readline

N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))

lines.sort()
s, e = lines[0][0], lines[0][1]
cnt = 0
for idx in range(1, N):
    x, y = lines[idx]
    if x > e:
        cnt += e - s
        s, e = x, y
    elif s <= x:
        if y > e:
            e = y

print(cnt + e - s)
