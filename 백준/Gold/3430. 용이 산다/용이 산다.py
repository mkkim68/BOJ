import sys
from heapq import heappop, heappush
input = sys.stdin.readline

Z = int(input())
for tc in range(Z):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lakes = [1] * (N+1)
    raindays = []  # 비가 오는 날만
    rain_lake = [[] for _ in range(N+1)]

    for i in range(M-1, -1, -1):
        if arr[i]:
            rain_lake[arr[i]].append(i)

    for lake in range(1, N+1):
        if rain_lake[lake]:
            when = rain_lake[lake].pop()
            heappush(raindays, (when, lake))

    ans = []
    for i in range(M):
        now = arr[i]
        if now == 0:  # 물 먹는 날
            if raindays:
                when, lake = heappop(raindays)
                lakes[lake] = 0
                ans.append(lake)
            else:
                ans.append(0)
        else:  # 비 오는 날
            if lakes[now] >= 1:
                print("NO")
                break
            else:
                lakes[now] = 1
            if rain_lake[now]:
                heappush(raindays, (rain_lake[now].pop(), now))
    else:
        print("YES")
        print(*ans, sep=' ')

# 1
# 2 6
# 0 0 1 0 1 2

# 1
# 2 6
# 0 0 0 1 0 1