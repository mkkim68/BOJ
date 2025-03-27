import sys
input = sys.stdin.readline

N = int(input())
now = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

delta = [-1, 0, 1]
ans = 1e9
temp1, temp2 = now[::], now[::]
cnt1, cnt2 = 0, 1
temp2[0] = (temp2[0] + 1) % 2
temp2[1] = (temp2[1] + 1) % 2
for i in range(1, N):
    if temp1[i-1] != goal[i-1]:
        cnt1 += 1
        temp1[i-1] = (temp1[i-1] + 1) % 2
        temp1[i] = (temp1[i] + 1) % 2
        if i < N-1:
            temp1[i+1] = (temp1[i+1] + 1) % 2

    if temp2[i-1] != goal[i-1]:
        cnt2 += 1
        temp2[i-1] = (temp2[i-1] + 1) % 2
        temp2[i] = (temp2[i] + 1) % 2
        if i < N-1:
            temp2[i+1] = (temp2[i+1] + 1) % 2

if temp1 == goal:
    ans = min(ans, cnt1)
if temp2 == goal:
    ans = min(ans, cnt2)

if ans < 1e9:
    print(ans)
else:
    print(-1)
