import sys
input = sys.stdin.readline

N = int(input())
E = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

stack = [1]
cnt = 0
while stack:
    s = stack.pop()
    if visited[s] == 0:
        visited[s] = 1
        cnt += 1
        for i in adj[s]:
            if visited[i] == 0:
                stack.append(i)

print(cnt-1)