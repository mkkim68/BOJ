import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def find_distance(start, trash):
    q = deque()
    visited = set()
    q.append([start, 0])
    while q:
        point, distance = q.popleft()
        r, c = point
        if point in visited:
            continue
        if point == trash:
            return distance
        visited.add(point)
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0<=nr<h and 0<=nc<w and (nr, nc) not in visited and board[nr][nc] != 'x':
                q.append([(nr, nc), distance+1])
    return -1


def backtracking(now, distance, cnt):
    global answer
    if distance >= answer:
        return
    if cnt == num:
        answer = min(answer, distance)
        return

    for next in range(1, num+1):
        if visited[next]:
            continue
        visited[next] = 1
        backtracking(next, distance + edges[now][next], cnt+1)
        visited[next] = 0


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    board = [list(input().strip()) for _ in range(h)]
    flag = 0

    # 로봇(0), 쓰레기(1~) 위치
    points = {}
    num = 0
    for r in range(h):
        for c in range(w):
            if board[r][c] == 'o':
                points[0] = (r, c)
            elif board[r][c] == '*':
                num += 1
                points[num] = (r, c)

    edges = [[1e9] * (len(points)) for j in range(len(points))]
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            point1, point2 = points[i], points[j]
            dis = find_distance(point1, point2)
            edges[i][j] = dis
            edges[j][i] = dis
            if dis == -1:
                print(-1)
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        continue

    answer = 1e9
    visited = [0] * (num+1)
    backtracking(0, 0, 0)
    print(answer)

