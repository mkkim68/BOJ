import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
words = {}
delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def dfs(start, w, now, cnt, points):
    global temp
    if now != w[:cnt]:
        return

    if now == w:
        temp += 1
        return

    for dr, dc in delta:
        nr, nc = (dr + start[0]+N)%N, (dc + start[1]+M)%M
        if board[nr][nc] == w[cnt]:
            dfs((nr, nc), w, now+[board[nr][nc]], cnt+1, points+[(nr, nc)])

for _ in range(K):
    word = input().strip()
    if word not in words:
        temp = 0
        for r in range(N):
            for c in range(M):
                if board[r][c] == word[0]:
                    visited = [[0] * M for _ in range(N)]
                    dfs((r, c), list(word), [word[0]], 1, [(r, c)])
        words[word] = temp

    print(words[word])