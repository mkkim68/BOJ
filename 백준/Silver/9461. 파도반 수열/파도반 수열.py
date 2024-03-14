import sys
input = sys.stdin.readline


def dp(n):
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n < 11:
        return p[n]
    else:
        for i in range(11, n+1):
            temp = p[i-1] + p[i-5]
            p.append(temp)
        return p[n]

T = int(input())
for tc in range(T):
    N = int(input())
    print(dp(N))