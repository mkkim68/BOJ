import sys
input = sys.stdin.readline

N = input().strip()
if len(N) < 2:
    N = '0' + N

cnt = 0
cur = N
while True:
    num = 0
    for n in cur:
        num += int(n)

    num = str(num)
    cur = cur[-1] + num[-1]
    cnt += 1
    if cur == N:
        print(cnt)
        break

