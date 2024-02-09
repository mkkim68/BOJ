import sys
input = sys.stdin.readline

def cut(n):
    p = [0] * (n+2)
    p[1] = 1
    p[2] = 2
    for i in range(3, n+1):
        p[i] = p[i-1] + p[i-2]

    return p[n]

N = int(input())

print(cut(N) % 10007)