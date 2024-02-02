import sys

input = sys.stdin.readline

N = int(input())
areas = []
area = []
ans = []
for _ in range(N):
    paper = set()
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            paper.add((i, j))
    areas.append(paper)
    area.append(w * h)

intersection = set()
for i in range(N-1, 0, -1):
    ans.append(len(areas[i]))
    intersection |= areas[i]
    areas[i-1] -= intersection

ans.append(len(areas[0]))
ans = ans[::-1]
print(*ans, sep='\n')