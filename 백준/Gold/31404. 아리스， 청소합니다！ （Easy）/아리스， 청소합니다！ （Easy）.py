import sys
input = sys.stdin.readline

H, W = map(int, input().split())
R, C, D = map(int, input().split())
rule_A = [list(map(int, input().strip())) for _ in range(H)]
rule_B = [list(map(int, input().strip())) for _ in range(H)]

delta = {0: (-1, 0),1: (0, 1), 2: (1, 0), 3: (0, -1)}
board = [[1] * W for _ in range(H)]
cnt = H * W
ans = 0
time = 0
MAX_TIME = H*W*8
while cnt > 0 and time - ans <= MAX_TIME:
    if board[R][C] == 1:
        board[R][C] = 0
        cnt -= 1
        ans = time+1
        D = (D + rule_A[R][C]) % 4
        dr, dc = delta[D][0], delta[D][1]
        nr, nc = R + dr, C + dc
        if 0 <= nr < H and 0 <= nc < W:
            R, C = nr, nc
        else:
            break
    else:
        D = (D + rule_B[R][C]) % 4
        dr, dc = delta[D][0], delta[D][1]
        nr, nc = R + dr, C + dc
        if 0 <= nr < H and 0 <= nc < W:
            R, C = nr, nc
        else:
            break
    time += 1

print(ans)
