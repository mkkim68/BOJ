import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(0)
else:
    ans = 0
    for ax in range(N):
        ay = arr[ax]
        cnt = 0

        for bx in range(ax):
            flag = True
            by = arr[bx]
            for cx in range(bx+1, ax):
                cy = arr[cx]
                D = ax*by + bx*cy + cx*ay - ax*cy - cx*by - bx*ay
                if D <= 0:
                    flag = False
            if flag:
                cnt += 1

        for bx in range(N-1, ax, -1):
            flag = True
            by = arr[bx]
            for cx in range(bx-1, ax, -1):
                cy = arr[cx]
                D = ax*by + bx*cy + cx*ay - ax*cy - cx*by - bx*ay
                if D >= 0:
                    flag = False
            if flag:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)