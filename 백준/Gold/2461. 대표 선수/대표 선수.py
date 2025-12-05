import sys
input = sys.stdin.readline

N, M = map(int, input().split())
classes = [sorted(list(map(int, input().split()))) for _ in range(N)]

idxs = [0] * N
ans = 1e9
while True:
    min_num, max_num = 1e9, 0
    min_idx = 0
    for i in range(N):
        idx = idxs[i]
        if classes[i][idx] < min_num:
            min_num = classes[i][idx]
            min_idx = i
        if classes[i][idx] > max_num:
            max_num = classes[i][idx]

    ans = min(ans, max_num - min_num)
    idxs[min_idx] += 1
    if idxs[min_idx] >= M:
        break

print(ans)