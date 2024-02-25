import sys
input = sys.stdin.readline


K, N = map(int, input().split())
lines = []
for i in range(K):
    lines.append(int(input()))
lines.sort()

e = lines[-1]
s = 1
m = (s + e) // 2
while s <= e:
    ans = 0
    for i in range(K):
        a = lines[i] // m
        ans += a
    if ans >= N:
        s = m+1
        m = (s + e) // 2
    else:
        e = m-1
        m = (s + e) // 2

print(m)