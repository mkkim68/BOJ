import sys
input = sys.stdin.readline


def rec(n):
    p = [0] * (n+1)
    p[1] = 1
    p[2] = 1
    for i in range(3, n+1):
        p[i] = p[i-1]+p[i-2]
    return p[n]


N = int(input())

print(f'{rec(N)} {N-2}')