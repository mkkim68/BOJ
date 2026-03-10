import sys
import bisect
input = sys.stdin.readline

L, N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def check(c):
    prev = 0
    for station in arr + [L]:
        if station - prev > c:
            return False
        prev = station

    last = 0
    cnt = 0
    while last + c < L:
        idx = bisect.bisect_right(arr, min(L, last+c))
        if idx == 0 or arr[idx - 1] <= last:
            return False

        last = arr[idx - 1]
        cnt += 1

        if cnt > K:
            return False

    return cnt <= K

cost = L+1
s, e = 1, L+1
while s <= e:
    m = (s + e) // 2
    if check(m):
        cost = min(cost , m)
        e = m - 1
    else:
        s = m + 1
print(cost)
