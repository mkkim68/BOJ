import sys
input = sys.stdin.readline

N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

if crains[0] < boxes[0]:
    print(-1)
else:
    time = 0
    used = [False] * M
    remaining = M

    while remaining > 0:
        time += 1
        box_idx = 0
        for c in crains:
            while box_idx < M and (used[box_idx] or boxes[box_idx] > c):
                box_idx += 1

            if box_idx < M:
                used[box_idx] = True
                remaining -= 1
                box_idx += 1

    print(time)