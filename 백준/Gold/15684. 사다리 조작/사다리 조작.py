import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

def check():
    for i in range(1, N+1):
        now = i
        for h in range(1, H+1):
            if board[h][now]:
                now += 1
            elif board[h][now-1]:
                now -= 1
        if now != i:
            return False

    return True

def dfs(cnt, x, y, target):
    if cnt == target:
        if check():
            print(target)
            exit()
        return

    for i in range(x, H+1):
        start_col = y if i == x else 1
        for j in range(start_col, N):
            if not board[i][j] and not board[i][j-1] and not board[i][j+1]:
                board[i][j] = 1
                dfs(cnt+1, i, j+2, target)
                board[i][j] = 0

for answer in range(4):
    dfs(0, 1, 1, answer)

print(-1)