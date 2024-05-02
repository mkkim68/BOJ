import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * (N+1)]

for _ in range(N):
    board.append([0]+list(map(int, input().split())))

for r in range(1, N+1):
    for c in range(1, N+1):
        board[r][c] += board[r][c-1]

for r in range(1, N+1):
    for c in range(1, N+1):
        board[c][r] += board[c-1][r]

for i in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    ans = board[r2][c2] - board[r1-1][c2] - board[r2][c1-1] + board[r1-1][c1-1]

    print(ans)