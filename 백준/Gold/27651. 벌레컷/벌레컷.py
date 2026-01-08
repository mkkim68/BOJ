import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 가슴 > 배 > 머리
prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

cnt = 0
for e in range(2, N):
    belly = prefix[N] - prefix[e]
    limit = min(belly, 2*prefix[e] - prefix[N])


    idx = bisect.bisect_left(prefix, limit, 1, e)
    cnt += idx - 1

print(cnt)