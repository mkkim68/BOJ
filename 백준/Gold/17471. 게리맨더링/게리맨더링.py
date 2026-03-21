import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
pops = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for i in range(N):
    n, *arr = list(map(int, input().split()))
    edges[i]=arr

total = sum(pops)
ans = 10000

def bfs(start, subset_a, subset_b):
    global ans
    q = deque()
    q.append(start)

    visited_a = [0] * N
    visited_a[start] = 1
    while q:
        now = q.popleft()
        for next in edges[now]:
            if visited_a[next-1]:
                continue
            if not subset_a[next-1]:
                continue
            q.append(next-1)
            visited_a[next-1] = 1

    visited_b = [0] * N
    for i in range(N):
        if b_mask[i]:
            q.append(i)
            visited_b[i] = 1
            break

    while q:
        now = q.popleft()
        for next in edges[now]:
            if visited_b[next - 1]:
                continue
            if not subset_b[next - 1]:
                continue
            q.append(next - 1)
            visited_b[next - 1] = 1
    if visited_a == subset_a and visited_b == subset_b:
        temp = 0
        for i in range(N):
            if visited_a[i]:
                temp += pops[i]
        ans = min(ans, abs(total - 2 * temp))

total_mask = (1 << N) - 1
used = set()
for a_mask in range(1 << N):
    b_mask = total_mask ^ a_mask
    if not a_mask:
        continue
    if a_mask in used or b_mask in used:
        break
    used.add(a_mask)
    used.add(b_mask)

    b_mask = list(map(int, bin(b_mask)[2:].zfill(N)))
    a_mask = list(map(int, bin(a_mask)[2:].zfill(N)))

    for i in range(N):
        is_included = a_mask[i]
        if is_included:
            bfs(i, a_mask, b_mask)
            break

if ans == 10000:
    print(-1)
else:
    print(ans)