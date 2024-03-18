import sys
input = sys.stdin.readline


def dp(n):
    if n == 1:
        return stairs[0]
    if n == 2:
        return stairs[0] + stairs[1]
    p = [stairs[0], stairs[0] + stairs[1], max(stairs[1] + stairs[2], stairs[0] + stairs[2])] + [0] * (n - 1)
    for i in range(3, n):
        p[i] = max(p[i-2] + stairs[i], p[i-3] + stairs[i-1] + stairs[i])
    return p[n - 1]


N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

print(dp(N))