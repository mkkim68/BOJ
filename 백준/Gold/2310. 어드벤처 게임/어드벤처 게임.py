import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur, money):
    global visited

    if rooms[cur] > 0:
        money = max(money, rooms[cur])
    else:
        money += rooms[cur]
        if money < 0:
            return False

    if cur == N:
        return True

    visited[cur] = 1
    for next in edges[cur]:
        if visited[next] == 0:
            if dfs(next, money):
                return True
    visited[cur] = 0
    return False



while True:
    N = int(input())

    if N == 0:
        break

    rooms = [0] # 방 정보
    edges = [[]]  # 방 연결 정보
    for i in range(1, N+1):
        info, cost, *next_rooms, end = input().strip().split()
        if info == 'T':
            rooms.append(-int(cost))
        else:
            rooms.append(int(cost))

        edges.append(list(map(int, next_rooms)))

    visited = [0] * (N+1)
    if dfs(1, 0):
        print("Yes")
    else:
        print("No")