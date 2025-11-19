import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

start = []
end = []
end_lie, is_lie = 0, 0 # 0: 세로, 1: 가로
for r in range(N):
    cnt = 0
    e_cnt = 0
    for c in range(N):
        if board[r][c] == 'B':
            start.append((r, c))
            if cnt > 0:
                is_lie = 1
            cnt += 1
        elif board[r][c] == 'E':
            end.append((r, c))
            if e_cnt > 0:
                end_lie = 1
            e_cnt += 1

q = deque()
ans = 1e9
visited = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
q.append(start+[is_lie])
r, c = start[1]
visited[r][c][is_lie] = 0
while q:
    b1, b2, b3, lie = q.popleft()
    if lie:
        r = b2[0]
        c1, c2, c3 = b1[1], b2[1], b3[1]
        tr, dr = r-1, r+1
        flag = 0 # 회전 가능 여부
        now = visited[r][c2][lie]
        if 0<=tr<N: # 위
            if board[tr][c1] != '1' and board[tr][c2] != '1' and board[tr][c3] != '1':
                flag += 1
                if visited[tr][c2][lie] == -1:
                    visited[tr][c2][lie] = now+1
                    q.append([(tr, c1), (tr, c2), (tr, c3), lie])
        if 0<=dr<N: # 아래
            if board[dr][c1] != '1' and board[dr][c2] != '1' and board[dr][c3] != '1':
                flag += 1
                if visited[dr][c2][lie] == -1:
                    visited[dr][c2][lie] = now+1
                    q.append([(dr, c1), (dr, c2), (dr, c3), lie])
        if 0<=c1-1<N and board[r][c1-1] != '1': # 왼
            if visited[r][c2-1][lie] == -1:
                visited[r][c2-1][lie] = now+1
                q.append([(r, c1-1), (r, c2-1), (r, c3-1), lie])
        if 0<=c3+1<N and board[r][c3+1] != '1': # 오른
            if visited[r][c2+1][lie] == -1:
                visited[r][c2+1][lie] = now+1
                q.append([(r, c1+1), (r, c2+1), (r, c3+1), lie])
        if flag == 2: # 회전
            new_b1 = (r-1, c2)
            new_b3 = (r+1, c2)
            if visited[r][c2][0] == -1:
                visited[r][c2][0] = now+1
                q.append([new_b1, b2, new_b3, 0])
    else:
        c = b2[1]
        r1, r2, r3 = b1[0], b2[0], b3[0]
        lc, rc = c - 1, c + 1
        flag = 0
        now = visited[r2][c][lie]
        if 0 <= lc < N:  # 왼
            if board[r1][lc] != '1' and board[r2][lc] != '1' and board[r3][lc] != '1':
                flag += 1
                if visited[r2][lc][lie] == -1:
                    visited[r2][lc][lie] = now+1
                    q.append([(r1, lc), (r2, lc), (r3, lc), lie])
        if 0 <= rc < N:  # 오
            if board[r1][rc] != '1' and board[r2][rc] != '1' and board[r3][rc] != '1':
                flag += 1
                if visited[r2][rc][lie] == -1:
                    visited[r2][rc][lie] = now+1
                    q.append([(r1, rc), (r2, rc), (r3, rc), lie])
        if 0 <= r1 - 1 < N and board[r1-1][c] != '1':  # 위
            if visited[r2-1][c][lie] == -1:
                visited[r2-1][c][lie] = now+1
                q.append([(r1-1, c), (r2-1, c), (r3-1, c), lie])
        if 0 <= r3 + 1 < N and board[r3+1][c] != '1':  # 아래
            if visited[r2+1][c][lie] == -1:
                visited[r2 + 1][c][lie] = now+1
                q.append([(r1+1, c), (r2+1, c), (r3+1, c), lie])
        if flag == 2:  # 회전
            new_b1 = (r2, c-1)
            new_b3 = (r2, c+1)
            if visited[r2][c][1] == -1:
                visited[r2][c][1]= now+1
                q.append([new_b1, b2, new_b3, 1])

r, c = end[1]
ans = visited[r][c][end_lie]
if ans == -1:
    print(0)
else:
    print(ans)