import sys
input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    # 시작 노드 초기화
    distance[start] = 0
    # 전체 v-1번의 라운드를 반복
    for i in range(V):
        # 매 반복마다 모든 간선 확인
        for j in range(E):
            cur_node = adj[j][0]
            next_node = adj[j][1]
            weight = adj[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[cur_node] + weight < distance[next_node]:
                distance[next_node] = distance[cur_node] + weight
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == V-1:
                    return True
    return False


V, E = map(int, input().split())
adj = []
distance = [INF] * (V+1)

for _ in range(E):
    s, e, w = map(int, input().split())
    adj.append([s, e, w])

ans = bellman_ford(1)
if ans:
    print(-1)
else:
    for i in range(2, V+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
  