import sys

input = sys.stdin.readline

N, K = map(int, input().split())

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

ans = fac(N) // (fac(N - K) * fac(K))

print(ans)

