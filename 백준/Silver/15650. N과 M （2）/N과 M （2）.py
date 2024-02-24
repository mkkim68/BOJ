import sys
input = sys.stdin.readline


def combination(idx, arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(idx+1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            combination(i, arr + [i])
            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N+1)
combination(0, [])