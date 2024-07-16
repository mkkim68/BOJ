import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(sr, sc):
    if visited[sr][sc] != 0:
        return visited[sr][sc]

    visited[sr][sc] = 1
    for dr, dc in delta:
        nr, nc = dr + sr, dc + sc
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > board[sr][sc]:
            visited[sr][sc] = max(visited[sr][sc], dfs(nr, nc) + 1)

    return visited[sr][sc]


visited = [[0] * N for _ in range(N)]

answer = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            temp = dfs(r, c)
            answer = max(answer, temp)

print(answer)