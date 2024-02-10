import sys
input = sys.stdin.readline


def people(k, n):
    floors = [list(i for i in range(1, n+1)) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(n):
            floors[i][j] = sum(floors[i-1][:j+1])

    return floors[-1][-1]


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(people(k, n))