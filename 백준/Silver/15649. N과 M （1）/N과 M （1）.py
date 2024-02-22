import sys
input = sys.stdin.readline


def permutation(arr):
    if len(arr) == M:
        print(*arr)
        return arr

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            permutation(arr+[nums[i]])
            visited[i] = 0


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
visited = [0] * N
permutation([])