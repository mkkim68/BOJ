import sys
input = sys.stdin.readline

N = int(input())
scores = [0] + [int(input().strip()) for _ in range(N)]

ans = 0
last = scores[-1]
for i in range(N-1, 0, -1):
    if scores[i] >= last:
        ans += scores[i] - last + 1
        scores[i] = last - 1

    last = scores[i]

print(ans)