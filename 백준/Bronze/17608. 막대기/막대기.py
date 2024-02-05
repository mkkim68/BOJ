import sys
input = sys.stdin.readline

N = int(input())
sticks = []
for _ in range(N):
    s = int(input())
    sticks.append(s)

ans = 0
max_s = 0
for i in range(N-1, -1, -1):
    if i == N-1:
        ans += 1
        max_s = sticks[i]
    elif sticks[i] < max_s:
        continue
    elif sticks[i] > max_s:
        ans += 1
        max_s = sticks[i]

print(ans)