import sys
input = sys.stdin.readline

def sol(arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in nums:
        sol(arr + [i])


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
sol([])