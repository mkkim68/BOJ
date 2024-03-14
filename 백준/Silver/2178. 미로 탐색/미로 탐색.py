import sys
from collections import deque
input = sys.stdin.readline

delta = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs(r, c):
    q = deque()
    q.append([(r, c)])
    cnt = 1
    while q:
        arr = q.popleft()
        temp = deque()
        for cur in arr:
            curr, curc = cur[0], cur[1]
            if visited[curr][curc] == 0:
                visited[curr][curc] = 1
                if curr == N-1 and curc == M-1:
                    return cnt
                for dr, dc in delta:
                    nr, nc = curr + dr, curc + dc
                    if 0<=nr<N and 0<=nc<M and maze[nr][nc] == 1 and visited[nr][nc] == 0:
                        temp.append((nr, nc))
        if temp:
            q.append(temp)
            cnt += 1


N, M = map(int, input().split())
maze = []
sr, sc = 0, 0
for j in range(N):
    arr = input().strip()
    t = []
    for i in range(M):
        a = int(arr[i])
        t.append(a)
    maze.append(t)

visited = [[0] * M for _ in range(N)]

ans = bfs(sr, sc)
print(ans)