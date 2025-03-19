import sys
from heapq import heappop, heappush
input = sys.stdin.readline


while True:
    N = int(input())

    if N == 0:
        break

    rooms = [0] # 방 정보
    edges = [[]]  # 방 연결 정보
    for i in range(1, N+1):
        info, cost, *next_rooms, end = input().strip().split()
        if info == 'L':
            rooms.append(-int(cost))
        else:
            rooms.append(int(cost))

        edges.append(list(map(int, next_rooms)))

    pq = []
    visited = [0] * (N + 1)
    heappush(pq, (0, 1))
    while pq:
        money, now = heappop(pq)
        if visited[now]:
            continue
        visited[now] = 1
        for next in edges[now]:
            if visited[next]:
                continue
            if rooms[next] > 0:
                if money + rooms[next] > 0:
                    continue
                heappush(pq, (money + rooms[next], next))
            else:
                heappush(pq, (min(money, rooms[next]), next))

    if visited[N]:
        print("Yes")
    else:
        print('No')
