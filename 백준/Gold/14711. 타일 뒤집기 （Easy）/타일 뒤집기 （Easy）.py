import sys
input = sys.stdin.readline

N = int(input())
first = input().strip()

if N == 1:
    print(first)
else:
    B = [[0]*N for _ in range(N)]

    for j in range(N):
        B[0][j] = 1 if first[j] == '#' else 0

    for j in range(N):
        v = 0
        if j > 0:
            v ^= B[0][j-1]
        if j < N-1:
            v ^= B[0][j+1]
        B[1][j] = v

    for i in range(1, N-1):
        for j in range(N):
            v = B[i-1][j]
            if j > 0:
                v ^= B[i][j-1]
            if j < N-1:
                v ^= B[i][j+1]
            B[i+1][j] = v

    for i in range(N):
        print(''.join('#' if B[i][j] else '.' for j in range(N)))