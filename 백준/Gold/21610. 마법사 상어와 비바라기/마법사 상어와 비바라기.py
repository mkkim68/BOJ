import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 처음 구름 좌표 (N-1, 0) (N-1, 1) (N-2, 0) (N-2, 1)
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
delta = [(-1,-1), (1, 1), (1, -1), (-1, 1)]
for _ in range(M):
    d, s = map(int, input().split())  # 구름이 d 방향으로 s칸 이동
    # print(cloud)
    if d == 1:  # ←
        move = (0, -1)
    elif d == 2:  # ↖
        move = (-1, -1)
    elif d == 3:  # ↑
        move = (-1, 0)
    elif d == 4:  # ↗
        move = (-1, 1)
    elif d == 5:  # →
        move = (0, 1)
    elif d == 6:  # ↘
        move = (1, 1)
    elif d == 7:  # ↓
        move = (1, 0)
    elif d == 8:  # ↙
        move = (1, -1)
    move_cloud = []
    for r, c in cloud:
        nr, nc = (move[0] * s + r) % N, (move[1] * s + c) % N
        A[nr][nc] += 1  # 각 구름에서 비가 내려 구름이 있는 칸 +1
        move_cloud.append((nr, nc))
    # 구름 사라짐
    # 물 증가한 칸에 물복사버그(대각선 방향 거리1인 칸에 물이 있는 칸 수만큼 증가)
    for r, c in move_cloud:
        cnt = 0
        for dr, dc in delta:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                cnt += 1
        A[r][c] += cnt
    # 물의 양 2 이상인 모든 칸에 구름 생성, 물양 -2 줄어듦, 3에서 구름 사라진 칸 빼고
    new_cloud = []
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and (r,c) not in move_cloud:
                new_cloud.append((r, c))
                A[r][c] -= 2
    cloud = new_cloud

ans = 0
for r in range(N):
    ans += sum(A[r])

print(ans)