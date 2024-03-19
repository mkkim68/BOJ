import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = [[0] * (K+1) for _ in range(N+1)]
for j in range(1, N+1):
    W, V = map(int, input().split())
    prev = p[j-1][:]
    for i in range(1, K+1):
        if i >= W:
            p[j][i] = max(prev[i], prev[i-W]+V)
        else:
            p[j][i] = prev[i]

print(p[-1][K])