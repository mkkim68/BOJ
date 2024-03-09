import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    result = input().strip()
    result = result.split("X")
    cnt = 0
    for o in result:
        if o:
            n = len(o)
            cnt += (1 + n) * n // 2
    print(cnt)
