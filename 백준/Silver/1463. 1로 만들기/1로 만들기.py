import sys
from collections import deque
input = sys.stdin.readline

def dp(n):
    visited = [0] * (n+1)
    q = deque()
    q.append([n, 0])
    cnts = []
    while q:
        n = q.popleft()
        if n[0] == 1:
            cnts.append(n[1])
            continue
        if visited[n[0]] == 0:
            visited[n[0]] = 1
            if n[0] % 3 == 0:
                n1 = n[0] // 3
                c1 = n[1] + 1
                q.append([n1, c1])
            if n[0] % 2 == 0:
                n2 = n[0] // 2
                c2 = n[1] + 1
                q.append([n2, c2])
            n3 = n[0] - 1
            c3 = n[1] + 1
            q.append([n3, c3])
    return min(cnts)

N = int(input())
print(dp(N))