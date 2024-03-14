import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # NxN 격자, 파이어볼 M개, K: 이동 명령 횟수
fire_balls = {}
board = [[[] for _ in range(N)] for j in range(N)]
for i in range(1, M+1):
    # r, c, m, s, d: r행 c열, 질량m, 방향d, 속력s
    r, c, m, s, d = map(int, input().split())
    fire_balls[i] = [r-1, c-1, m, s, d]
    board[r-1][c-1].append(i)

# d: 0-7 (북 동북 동 동남 남 서남 서 북서)
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
last = M
# print(fire_balls)
for k in range(K):
    # 자신의 방향 d로 속력 s만큼 이동
    temp = []
    for fireball in fire_balls:
        r, c, m, s, d = fire_balls[fireball]
        dr, dc = delta[d]
        nr, nc = (dr * s + r) % N, (dc*s + c) % N
        fire_balls[fireball] = [nr, nc, m, s, d]
        board[r][c].remove(fireball)
        board[nr][nc].append(fireball)
    # 같은 칸에 있는 파이어볼 하나로 합치고 나누기
    for r in range(N):
        for c in range(N):
            if len(board[r][c]) >= 2:
                mass, speed, direc = 0, 0, []
                for i in board[r][c]:
                    info = fire_balls[i]
                    mass += info[2]
                    speed += info[3]
                    direc.append(info[4])
                    del fire_balls[i]
                odd, even = 0, 0
                for d in direc:
                    cur = 0
                    if d % 2 == 0:
                        cur = 'even'
                        even += 1
                    else:
                        cur = 'odd'
                        odd += 1
                    if (odd > 0 and cur == 'even') or (even >0 and cur == 'odd'):
                        new_d = [1, 3, 5, 7]
                        break
                else:
                    new_d = [0, 2, 4, 6]
                mass //= 5
                speed //= len(board[r][c])
                board[r][c].clear()
                if mass > 0:
                    for i in range(4):
                        last += 1
                        board[r][c].append(last)
                        fire_balls[last] = [r, c, mass, speed, new_d[i]]

ans = 0
for fireball in fire_balls:
    ans += fire_balls[fireball][2]

print(ans)