import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    global ans
    visited[now] = 1
    cycle_list.append(now)
    next = students[now]

    if visited[next] == 1:
        if next in cycle_list:
            ans -= len(cycle_list[cycle_list.index(next):])
        return

    else:
        dfs(next)

T = int(input())
for tc in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    ans = n

    for i in range(1, n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)

    print(ans)

