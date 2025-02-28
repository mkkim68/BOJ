import sys
input = sys.stdin.readline

N = int(input())
ans = [[0] * N for _ in range(N)]
edges = [list(map(int, input().split()))for _ in range(N)]

for i in range(N):
    visited = [0] * N
    stack = [i]
    while stack:
        now = stack.pop()
        for j in range(N):
            is_way = edges[now][j]
            if is_way and visited[j] == 0:
                stack.append(j)
                ans[i][j] = 1
                visited[j] = 1

for a in ans:
    print(*a)