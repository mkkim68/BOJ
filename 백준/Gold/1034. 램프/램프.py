import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
K = int(input())

rows = {}
possibles = set()
cnts = set()
for b in board:
    now = tuple(b)
    if now in rows:
        rows[now] += 1
    else:
        rows[now] = 1
        cnt = b.count(0)
        if cnt in cnts:
            possibles.add(now)
            continue

        if K >= cnt and (K - cnt) % 2 == 0: # 짝수
            cnts.add(cnt)
            possibles.add(now)

ans = 0
for p in possibles:
    ans = max(ans, rows[p])

print(ans)