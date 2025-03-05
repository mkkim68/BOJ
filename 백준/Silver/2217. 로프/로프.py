import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()
ans = 0
for i in range(N):
    ans = max(ans, ropes[i]*(N-i))

print(ans)