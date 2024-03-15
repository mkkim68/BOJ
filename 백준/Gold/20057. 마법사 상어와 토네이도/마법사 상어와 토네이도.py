import sys
from collections import deque
input = sys.stdin.readline


def storm(r, c, dr, dc, nr, nc):
    sand = A[nr][nc]
    A[nr][nc] = 0
    out = 0
    out += sand // 20
    out += sand * 7 // 100
    out += sand // 10
    out += sand // 100
    out += sand * 2 // 100
    out += sand * 7 // 100
    out += sand // 10
    out += sand // 100
    out += sand * 2 // 100
    if 0 <= r + 3*dr < N and 0 <= c + 3*dc < N:  # 5%
        A[r + 3*dr][c + 3*dc] += sand // 20
    if dr == 0:
        if 0 <= r+1 < N:
            A[r+1][c] += sand // 100  # 1%
            if 0 <= c + dc < N:  # 7%
                A[r+1][c+dc] += sand * 7 // 100
            if 0 <= c + 2 * dc < N:  # 10%
                A[r+1][c + 2 * dc] += sand // 10
        if 0 <= r+2 < N and 0 <= c + dc < N:  # 2%
            A[r+2][c+dc] += sand * 2 // 100
        if 0 <= r-1 < N:
            A[r-1][c] += sand//100
            if 0 <= c + dc < N:
                A[r-1][c+dc] += sand * 7 // 100
            if 0 <= c + 2 * dc < N:
                A[r-1][c + 2 * dc] += sand // 10
        if 0 <= r-2 < N and 0 <= c + dc < N:
            A[r-2][c+dc] += sand * 2 // 100
    elif dc == 0:
        if 0 <= c + 1 < N:
            A[r][c+1] += sand // 100
            if 0 <= r + dr < N:
                A[r + dr][c + 1] += sand * 7 // 100
            if 0 <= r + 2 * dr < N:
                A[r + 2*dr][c + 1] += sand // 10
        if 0 <= c + 2 < N and 0 <= r + dr < N:
            A[r + dr][c + 2] += sand * 2 // 100
        if 0 <= c - 1 < N:
            A[r][c-1] += sand // 100
            if 0 <= r + dr < N:
                A[r + dr][c - 1] += sand * 7 // 100
            if 0 <= r + 2 * dr < N:
                A[r + 2*dr][c -1] += sand // 10
        if 0 <= c - 2 < N and 0 <= r + dr < N:
            A[r + dr][c - 2] += sand * 2 // 100
    if 0 <= r + 2 * dr < N and 0 <= c + 2 * dc < N:  # α
        A[r + 2 * dr][c + 2 * dc] += (sand - out)
    return


N = int(input())
A = []
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    for c in row:
        if c:
            total += c
    A.append(row)

delta = deque([(0,-1), (1,0), (0, 1), (-1, 0)]) # 좌하우상

curr, curc = N//2, N//2
for i in range(1, N+1):
    d = delta[0]
    dr, dc = d[0], d[1]
    for j in range(i):
        nr, nc = curr + dr, curc + dc
        # 모래 흩날리기
        storm(curr, curc, dr, dc, nr, nc)
        curr, curc = nr, nc
        if curr == curc == 0:
            break
    else:
        delta.rotate(-1)
        d = delta[0]
        dr, dc = d[0], d[1]
        for j in range(i):
            nr, nc = curr + dr, curc + dc
            # 모래 흩날리기
            storm(curr, curc, dr, dc, nr ,nc)
            curr, curc = nr, nc
    delta.rotate(-1)

ans = 0
for r in range(N):
    for c in range(N):
        if A[r][c]:
            ans += A[r][c]

print(total - ans)