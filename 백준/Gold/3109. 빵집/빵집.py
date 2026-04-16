import sys
# 재귀 깊이를 적당히 조절 (R이 10,000이니 20,000 정도면 충분합니다)
sys.setrecursionlimit(20000)
input = sys.stdin.readline

R, C = map(int, input().split())
# board를 수정하면서 방문 체크를 대신합니다.
board = [list(input().strip()) for _ in range(R)]
cnt = 0

def dfs(r, c):
    if c == C - 1:
        return True

    for dr in [-1, 0, 1]:
        nr, nc = r + dr, c + 1
        
        if 0 <= nr < R and board[nr][nc] == '.':
            board[nr][nc] = 'x'
            if dfs(nr, nc):
                return True
                
    return False

for r in range(R):
    if board[r][0] == '.':
        board[r][0] = 'x'
        if dfs(r, 0):
            cnt += 1

print(cnt)