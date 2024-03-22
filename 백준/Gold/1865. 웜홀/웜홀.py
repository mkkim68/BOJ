import sys
input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(len(adj)):
            now, to, cost = adj[j][0], adj[j][1], adj[j][2]
            if distance[now] + cost < distance[to]:
                distance[to] = distance[now] + cost
                if i == N-1:
                    return "YES"
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N, M, W = map(int, input().split())  # 노드 개수, 도로 개수, 웜홀 개수
    adj = []
    for _ in range(M):  # 도로
        s, e, w = map(int, input().split())
        adj.append([s, e, w])
        adj.append([e, s, w])
    for _ in range(W):  # 웜홀
        s, e, w = map(int, input().split())
        w = -w
        for arr in adj:
            if arr[0] == s and arr[1] == e:
                adj.remove(arr)
                break
        adj.append([s, e, w])
    distance = [INF] * (N + 1)
    # print(adj)
    ans = bf(1)
    # print(distance)
    print(ans)
