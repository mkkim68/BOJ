import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
check = []
ans = 0
for _ in range(N):
    S.add(str(input()))

for _ in range(M):
    check.append(str(input()))

for s in check:
    if s in S:
        ans += 1

print(ans)
