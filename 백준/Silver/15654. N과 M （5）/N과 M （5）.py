import sys
from collections import deque
input = sys.stdin.readline


def per(arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            per(arr + [nums[i]])
            visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N
per([])
