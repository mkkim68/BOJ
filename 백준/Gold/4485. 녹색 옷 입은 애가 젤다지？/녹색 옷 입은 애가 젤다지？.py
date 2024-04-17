import sys
from heapq import heappop, heappush
input = sys.stdin.readline


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    pq = []
    costs = [[1e9] * N for _ in range(N)]
    heappush(pq, (board[0][0], (0, 0)))
    costs[0][0] = board[0][0]
    while pq:
        cost, now = heappop(pq)
        r, c = now[0], now[1]
        if costs[r][c] < cost:
            continue

        costs[r][c] = cost
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cost + board[nr][nc]
                if next_cost >= costs[nr][nc]:
                    continue
                heappush(pq, (next_cost, (nr, nc)))
                costs[nr][nc] = next_cost

    ans = costs[N - 1][N - 1]
    print(f'Problem {cnt}: {ans}')
    cnt += 1