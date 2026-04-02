import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sol():
    visited = [[set() for _ in range(C)] for _ in range(R)]

    start_mask = 1 << board[0][0]
    q = {(0, 0, start_mask, 1)}
    visited[0][0].add(start_mask)

    max_dist = 1

    while q:
        r, c, mask, dist = q.pop()

        if dist > max_dist:
            max_dist = dist

        if max_dist == 26:
            return 26

        for dr, dc in delta:
            nr, nc = dr + r, dc + c

            if 0 <= nr < R and 0 <= nc < C:
                char_bit = 1 << board[nr][nc]

                if not (mask & char_bit):
                    next_mask = mask | char_bit

                    if next_mask not in visited[nr][nc]:
                        visited[nr][nc].add(next_mask)
                        q.add((nr, nc, next_mask, dist + 1))

    return max_dist

print(sol())
