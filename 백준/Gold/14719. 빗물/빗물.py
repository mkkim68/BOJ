import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = list(map(int, input().split()))

ans = 0
for i in range(1, W-1):
    ml = max(board[:i])
    mr = max(board[i+1:])
    m = min(ml, mr)
    ans += max(0, m - board[i])
    
print(ans)