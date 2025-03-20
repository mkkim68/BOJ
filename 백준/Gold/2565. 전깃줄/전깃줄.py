import sys
import bisect
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

lines.sort()

lis = []

for i in range(N):
    num = lines[i][1]
    idx = bisect.bisect_left(lis, num)

    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(N - len(lis))