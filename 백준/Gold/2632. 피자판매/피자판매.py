import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
m, n = map(int, input().split())
a_sizes = list(int(input()) for _ in range(m))
b_sizes = list(int(input()) for _ in range(n))

a_prefix = [a_sizes[0]]
b_prefix = [b_sizes[0]]
for i in range(1, 2*m):
    s = a_prefix[i-1] + a_sizes[i%m]
    a_prefix.append(s)

for i in range(1, 2*n):
    s = b_prefix[i-1] + b_sizes[i%n]
    b_prefix.append(s)

sumA = []
sumB = []
cnt = 0
totalA, totalB = sum(a_sizes), sum(b_sizes)
if totalA == T:
    cnt += 1
elif totalA < T:
    sumA.append(totalA)

if totalB == T:
    cnt += 1
elif totalB < T:
    sumB.append(totalB)

for i in range(m):
    for j in range(i+1, min(2*m, i+m)):
        p = a_prefix[j] - a_prefix[i]
        if p < T:
            sumA.append(p)
        elif p == T:
            cnt += 1

for i in range(n):
    for j in range(i+1, min(2*n, i+n)):
        p = b_prefix[j] - b_prefix[i]
        if p < T:
            sumB.append(p)
        elif p == T:
            cnt += 1

sumB.sort()
for now in sumA:
    l, r = bisect_left(sumB, T-now), bisect_right(sumB, T-now)
    cnt += r - l

print(cnt)