import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x

    return find(parents[x])

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N, M = map(int, input().split())
parents = [i for i in range(N+1)]
cnt = 0
set_count = set()
for _ in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cnt += 1
    else:
        union(a, b)

for i in range(1, N+1):
    set_count.add(find(i))

print(cnt + len(set_count) - 1)