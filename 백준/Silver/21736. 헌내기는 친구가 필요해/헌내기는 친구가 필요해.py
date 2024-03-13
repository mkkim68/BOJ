import sys
from collections import deque
input = sys.stdin.readline

delta = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs(r, c):
    q = deque()
    q.append((r, c))
    cnt = 0
    while q:
        cur = q.popleft()
        curr, curc = cur[0], cur[1]
        if visited[curr][curc] == 0:
            visited[curr][curc] = 1
            if campus[curr][curc] == 'P':
                cnt += 1
            for dr, dc in delta:
                nr, nc = curr + dr, curc + dc
                if 0<=nr<N and 0<=nc<M and campus[nr][nc] != 'X' and visited[nr][nc] == 0:
                    q.append((nr, nc))
    return cnt


N, M = map(int, input().split())
campus = []
sr, sc = 99, 99
for j in range(N):
    arr = input().strip()
    temp = []
    for i in range(M):
        a = arr[i]
        temp.append(a)
        if a == 'I':
            sr, sc = j, i
    campus.append(temp)

visited = [[0] * M for _ in range(N)]

ans = bfs(sr, sc)
if ans:
    print(ans)
else:
    print('TT')