import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # N: 땅 길이, M: 구매한 나무 수, K: 년

A = [[0] * (N+1)]  # 양분 정보
for _ in range(N):
    a = [0] + list(map(int, input().split()))
    A.append(a)

ground = [[[] for i in range(N+1)] for _ in range(N+1)] # 땅 정보
for _ in range(M):
    x, y, z = map(int, input().split())
    ground[x][y].append(z)

# 봄: 어린나이부터 양분, 나이만큼 양분 못먹으면 죽음, 양분먹으면 +1살
# 여름: 죽은 나무가 양분이 됨 (나이//2)
# 가을: 나무 번식, 나이가 5의 배수인 나무만 인접한 8개 칸에 나이가 1인 나무 생성
# 겨울: 땅에 양분 추가, 양분의 양(A[r][c])
# K년 뒤 살아있는 나무 개수
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
nutrition = [[5] * (N+1) for _ in range(N+1)]

for year in range(K):
    temp = [[0] * (N+1) for _ in range(N+1)]
    for season in range(1, 5):
        if season == 1:  # 봄
            for r in range(1, N+1):
                for c in range(1, N+1):
                    ground[r][c].sort(reverse=True)
                    tree_num = len(ground[r][c])
                    for idx in range(tree_num-1, -1, -1):
                        tree = ground[r][c][idx]
                        if nutrition[r][c] >= tree:
                            nutrition[r][c] -= tree
                            ground[r][c][idx] += 1
                        else:
                            temp[r][c] += ground[r][c][idx] // 2
                            ground[r][c].remove(ground[r][c][idx])
        elif season == 2:  # 여름
            for r in range(1, N+1):
                for c in range(1, N+1):
                    nutrition[r][c] += temp[r][c]
        elif season == 3:  # 가을
            for r in range(1, N+1):
                for c in range(1, N+1):
                    tree_num = len(ground[r][c])
                    for idx in range(tree_num):
                        tree = ground[r][c][idx]
                        if tree % 5 == 0:
                            for dr, dc in delta:
                                nr, nc = r+dr, c+dc
                                if 1<=nr<=N and 1<=nc<=N:
                                    ground[nr][nc].append(1)
        elif season == 4:  # 겨울
            for r in range(1, N+1):
                for c in range(1, N+1):
                    nutrition[r][c] += A[r][c]

cnt = 0
for r in range(1, N+1):
    for c in range(1, N+1):
        cnt += len(ground[r][c])

print(cnt)