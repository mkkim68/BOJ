import sys
input = sys.stdin.readline


def cut(n):
    p = [0] * (n+2)
    p[1] = 1
    p[2] = 3
    for i in range(3, n+2):
        p[i] = p[i-1] + 2 * p[i-2]

    return p[n]


n = int(input())

print(cut(n) % 10007)