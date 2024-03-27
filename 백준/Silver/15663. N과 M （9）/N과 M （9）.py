import sys
input = sys.stdin.readline


def sol(arr):
    if tuple(arr) in visited:
        return

    if len(arr) == M:
        print(*arr)
        visited.add(tuple(arr))
        return

    for i in range(N):
        # print(i, N)
        if temp[i] == 0:
            temp[i] = 1
            sol(arr+[nums[i]])
            temp[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = set()
temp = [0] * N

sol([])