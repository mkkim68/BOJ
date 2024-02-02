import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * 1001 for i in range(1001)]
areas = []
for n in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            board[i][j] = n

for n in range(1, N+1):
    area = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == n:
                area += 1
    areas.append(area)

print(*areas, sep='\n')
