import sys
input = sys.stdin.readline


def combination(idx, arr):
    global ans
    if len(arr) == M:
        temp = []
        cnt = []
        for r, c in arr:
            temp.append(chicken(r, c))
        for j in range(len(temp[0])):
            t = []
            for i in range(M):
                t.append(temp[i][j])
            cnt.append(min(t))
        ans = min(sum(cnt), ans)
        return

    for i in range(idx, len(chickens)):
        if visited[i] == 0:
            visited[i] = 1
            combination(i+1, arr + [chickens[i]])
            visited[i] = 0


def chicken(row, col):
    arr = []
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                arr.append(abs(r-row) + abs(c-col))
    return arr


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens = []
cnt = 0
for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chickens.append((r,c))

visited = [0] * len(chickens)
ans = 1e9
combination(0, [])
print(ans)