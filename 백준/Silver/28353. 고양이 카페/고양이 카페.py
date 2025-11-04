import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cats = list(map(int, input().split()))
cats.sort()

ans = 0
s, e = 0, N-1
while s < e:
    temp = cats[s] + cats[e]
    if temp <= K:
        ans += 1
        s += 1
        e -= 1
    else:
        e -= 1

print(ans)