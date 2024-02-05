import sys
input = sys.stdin.readline

heights = []
for _ in range(9):
    heights.append(int(input()))

ans = []
for i in range(1<<9):
    temp = []
    for j in range(9):
        if i & (1<<j):
            temp.append(heights[j])
    if len(temp) == 7:
        ans.append(temp)

for h in ans:
    if sum(h) == 100:
        h.sort()
        print(*h, sep='\n')
        break