import sys
input = sys.stdin.readline


def calc(arr):
    cnt = S[arr[0]][arr[1]]
    return cnt


def permutation(idx, g, arr):
    if len(arr) == 2:
        people[idx] += calc(arr)
        return

    for i in range(N//2):
        if visited[i] == 0:
            visited[i] = 1
            permutation(idx, g, arr + [g[i]])
            visited[i] = 0


def combination(idx, arr):
    if len(arr) == N//2:
        groups.append(arr)
        return

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            combination(i+1, arr + [i])
            visited[i] = 0


N = int(input())
S = []
for i in range(N):
    S.append(list(map(int, input().split())))

groups = []
visited = [0] * N
combination(0, [])
people = [0] * len(groups)
for i in range(len(groups)):
    group = groups[i]
    permutation(i, group, [])

min_ans = 1e9
for idx in range(len(groups)//2):
    a, b = people[idx], people[len(groups)-idx-1]
    if abs(a-b) < min_ans:
        min_ans = abs(a-b)
        
print(min_ans)