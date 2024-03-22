import sys
from collections import deque
input = sys.stdin.readline


def bfs(row, col):
    q = deque()
    q.append((row, col))
    cnt = 0
    while q:
        r, c = q.popleft()
        if visited[r][c] == 0:
            cnt += 1
            visited[r][c] = 1
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0<=nr<2**N and 0<=nc<2**N and A[nr][nc] > 0 and visited[nr][nc] == 0:
                    q.append((nr, nc))
    return cnt


N, Q = map(int, input().split())
A = []
for _ in range(2**N):
    A.append(list(map(int, input().split())))
L = list(map(int, input().split()))

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(Q):
    l = L[i]
    level = 2**l
    # 90도 회전
    for r in range(0,2**N-level+1,level):
        for c in range(0,2**N-level+1,level):
            sr, er, sc, ec = r, r+level, c, c+level
            temp = [[] for _ in range(level)]
            for cr in range(sr, er):
                for cc in range(sc, ec):
                    temp[cr-r].append(A[cr][cc])
            new = list(zip(*temp))
            for j in range(level):
                row = list(new[j])
                row.reverse()
                new[j] = row
            for cr in range(sr, er):
                for cc in range(sc, ec):
                    A[cr][cc] = new[cr-r][cc-c]

    # 얼음이 있는 칸 3개 이상과 인접x인지
    points = []
    for r in range(2**N):
        for c in range(2**N):
            cnt = 0
            for dr, dc in delta:
                nr, nc = dr+r, dc+c
                if 0<=nr<2**N and 0<=nc<2**N and A[nr][nc] > 0:
                    cnt += 1
            if cnt < 3:
                points.append((r, c))
    # 얼음 녹이기
    for r, c in points:
        A[r][c] -= 1

# print(*A, sep='\n')
ans = 0
visited = [[0] * (2**N) for _ in range(2**N)]
for r in range(2**N):
    for c in range(2**N):
        if visited[r][c] == 1 or A[r][c] <= 0:
            continue
        a = bfs(r, c)
        ans = max(ans, a)


ice = 0
for r in range(2**N):
    for c in range(2**N):
        if A[r][c] > 0:
            ice += A[r][c]

print(ice)
print(ans)
