import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(5)]

points = [(i, j) for i in range(5) for j in range(5)]
visited = [0] * 25
ans = 0

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def check(arr):
    q = deque([arr[0]])
    arr.pop(0)
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if (nr, nc) in arr:
                q.append((nr, nc))
                arr.remove((nr, nc))

    if len(arr) == 0:
        return True
    return False


def combi(arr, idx, Y_cnt):
    global ans
    if Y_cnt >= 4:
        return

    if len(arr) == 7:
        if check(sorted(arr)):
            ans += 1
        return

    for i in range(idx, 25):
        if visited[i] == 0:
            visited[i] = 1
            if board[points[i][0]][points[i][1]] == 'Y':
                combi(arr+[points[i]], i+1, Y_cnt + 1)
            else:
                combi(arr + [points[i]], i + 1, Y_cnt)
            visited[i] = 0


combi([], 0, 0)
print(ans)
