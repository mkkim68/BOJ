import sys
input = sys.stdin.readline
# 땅의 면적 N * M, 인벤토리에 가진 블록의 개수 B
N, M, B = map(int, input().split())
ground = []
for i in range(N):
    row = list(map(int, input().split()))
    ground.extend(row)

ans = []
# key: 높이, value: 갯수
for key in range(0, 257):
    time = 0
    b = B
    for i in range(N*M):
        if ground[i] > key:  # 블럭이 기준높이보다 높을 때
            time += 2 * (ground[i] - key)
            b += ground[i] - key
        elif ground[i] < key:  # 블럭이 기준높이보다 낮을 때
            b -= key - ground[i]
            time += key - ground[i]
    if b < 0:
        continue
    ans.append([time, key])

ans.sort(key=lambda x: (x[0], -x[1]))

print(ans[0][0], ans[0][1])
