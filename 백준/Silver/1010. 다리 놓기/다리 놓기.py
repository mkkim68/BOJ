T = int(input())
for i in range(0, T):
    N, M = map(int, input().split())
    A = 1
    for j in range(1, M+1):
        A *= j
    for k in range(1, N+1):
        A //= k
    for m in range(1, M-N+1):
        A //= m
    print(int(A))
