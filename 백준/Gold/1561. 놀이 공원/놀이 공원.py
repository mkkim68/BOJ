import sys
from math import gcd
input = sys.stdin.readline

N, M = map(int, input().split())  # 아이들 수, 놀이기구 수
arr = list(map(int, input().split()))

if N <= M:
    print(N)
else:
    l, r = 0, N * 30
    t = None
    while l <= r:
        mid = (l + r) // 2
        cnt = M
        for i in range(M):
            cnt += mid // arr[i]
        if cnt >= N:
            t = mid
            r = mid - 1
        else:
            l = mid + 1

    cnt = M
    for i in range(M):
        cnt += (t-1) // arr[i]

    for i in range(M):
        if t % arr[i] == 0:
            cnt += 1
        if cnt == N:
            print(i+1)
            break
