import sys
input = sys.stdin.readline


def permutation(arr, idx):
    global ans
    if len(arr) == M:
        if tuple(arr) not in ans:
            ans.add(tuple(arr))
        return

    for i in range(idx, N+1):
        if visited[i] == 0:
            visited[i] = 1
            permutation(arr + [i], i+1)
            visited[i] = 0
            permutation(arr + [i], i)


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
visited = [0] * (N+1)
ans = set()
permutation([], 1)
ans = sorted(list(ans))
for a in ans:
    print(*a)