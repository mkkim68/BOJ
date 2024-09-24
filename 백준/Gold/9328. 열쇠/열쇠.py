import sys
from collections import deque
input = sys.stdin.readline

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(sr, sc):
    global keys, ans
    q = deque()
    doors = {chr(i): [] for i in range(65, 91)}
    q.append((sr, sc))
    visited = set()
    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0 <= nr < H+2 and 0 <= nc < W+2 and (nr, nc) not in visited:
                if board[nr][nc] == '*':
                    continue
                elif 'A' <= board[nr][nc] <= 'Z' and board[nr][nc] not in keys:
                    doors[board[nr][nc]].append((nr, nc))
                    continue
                elif 'a' <= board[nr][nc] <= 'z':  # 키
                    keys.add(board[nr][nc].upper())
                    if board[nr][nc].upper() in doors:
                        for point in doors[board[nr][nc].upper()]:
                            q.append((point[0], point[1]))
                        del doors[board[nr][nc].upper()]
                    board[nr][nc] = '.'
                elif board[nr][nc] == '$':
                    ans += 1
                    board[nr][nc] = '.'

                q.append((nr, nc))


T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    board = [['.'] * (W+2)] + [['.'] + list(input().strip()) + ['.'] for _ in range(H)] + [['.'] * (W+2)]
    temp = input().strip()

    keys = set()
    if temp != '0':
        for t in temp:
            keys.add(t.upper())

    # print(keys)
    # for b in board:
    #     print(b)

    ans = 0

    bfs(0, 0)
    print(ans)