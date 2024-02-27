import sys
input = sys.stdin.readline


def combination(idx, arr):
    if len(arr) == 6:
        print(*arr)
        return

    for i in range(idx, k):
        if visited[i] == 0:
            visited[i] = 1
            combination(i+1, arr + [S[i]])
            visited[i] = 0


while True:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    else:
        k, S = a[0], a[1:]
        visited = [0] * (k+1)
        combination(0, [])
        print()