import sys
input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())
paper = [list(0 for _ in range(W)) for _ in range(H)]
ans = []
temp1 = []
temp2 = []
history = {0:[], 1:[]}
for _ in range(N):
    dir, num = map(int, input().split())
    # 가로: 0 ,세로: 1
    history[dir] += [num]

history[0].sort()
history[1].sort()


for h in range(len(history[0])):
    if not temp1:
        temp1.append(history[0][h])
    else:
        temp1.append(abs(history[0][h] - history[0][h-1]))
    if h == len(history[0])-1:
        temp1.append(H - history[0][h])

for w in range(len(history[1])):
    if not temp2:
        temp2.append(history[1][w])
    else:
        temp2.append(abs(history[1][w] - history[1][w-1]))
    if w == len(history[1])-1:
        temp2.append(W - history[1][w])

if history[0] and history[1]:
    for i in temp1:
        for j in temp2:
            ans.append(i * j)
    print(max(ans))
elif not history[0] and history[1]:
    for j in temp2:
        ans.append(H * j)
    print(max(ans))
elif not history[1] and history[0]:
    for i in temp1:
        ans.append(W * i)
    print(max(ans))
else:
    print(W * H)


