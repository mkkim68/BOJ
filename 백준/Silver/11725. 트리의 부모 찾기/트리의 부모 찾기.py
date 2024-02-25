import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

visited = [0] * (N+1)
par = [0] * (N+1)
stack = [1]
while stack:
    s = stack.pop()
    if visited[s] == 0:
        visited[s] = 1
        # print(s)
        for i in arr[s]:
            if visited[i] == 0:
                par[i] = s
                stack.append(i)

for p in par[2:]:
    print(p)