import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
min_h, max_h = 1, trees[-1]
answer = 0
while min_h <= max_h:
    center = (min_h + max_h) // 2
    cnt = 0
    for t in trees:
        if center < t:
            cnt += t - center
    if cnt >= M:
        answer = max(center, answer)
        min_h = center + 1
    elif cnt < M:
        max_h = center-1

print(answer)
