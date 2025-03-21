import sys
input = sys.stdin.readline

N, K, R = map(int, input().split())
road = {}
for _ in range(R):
    r, c, rr, cc = map(int, input().split())
    if (r-1, c-1) not in road:
        road[(r-1, c-1)] = {(rr-1, cc-1)}
    else:
        road[(r-1, c-1)].add((rr-1, cc-1))
    if (rr-1, cc-1) not in road:
        road[(rr-1, cc-1)] = {(r - 1, c - 1)}
    else:
        road[(rr-1, cc-1)].add((r-1, c-1))

cows = []
for _ in range(K):
    r, c = map(int, input().split())
    cows.append((r-1, c-1))


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(start, end):
    stack = [start]
    visited = [[0] * N for _ in range(N)]
    while stack:
        r, c = stack.pop()

        if visited[r][c]:
            continue

        if (r, c) == end:
            return True

        visited[r][c] = 1
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0<=nr<N and 0 <=nc<N:
                if (r, c) in road:
                    if (nr, nc) not in road[(r,c)] and not visited[nr][nc]:
                        stack.append((nr, nc))
                else:
                    stack.append((nr, nc))

    return False

ans = 0
for i in range(K-1):
    for j in range(i+1, K):
        if not dfs(cows[i], cows[j]):
            ans += 1

print(ans)

