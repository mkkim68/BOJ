import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs():
    q = deque()
    q.append(S)
    visited = [-1] * (F+1)
    visited[S] = 0
    while q:
        now = q.popleft()
        if now == G:
            return visited[now]

        next_up = now + U
        next_down = now - D

        if 1 <= next_up <= F and visited[next_up] == -1:
            visited[next_up] = visited[now] + 1
            q.append(next_up)

        if 1 <= next_down <= F and visited[next_down] == -1:
            visited[next_down] = visited[now] + 1
            q.append(next_down)

    return -99

ans = bfs()
if ans == -99:
    print('use the stairs')
else:
    print(ans)
