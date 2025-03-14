import sys
input = sys.stdin.readline

N = int(input())
board = [input().split() for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
teachers = []
blanks = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 'X':
            blanks.append((r, c))
        elif board[r][c] == 'T':
            teachers.append((r, c))

def check(arr):
    for tr, tc in teachers:
        for dr, dc in delta:
            stack = [(tr, tc)]
            while stack:
                r, c = stack.pop()
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == "S":
                        return False
                    elif (nr, nc) in arr:
                        break
                    stack.append((nr, nc))

    return True


visited = [0] * len(blanks)
def combi(idx, arr):
    global visited

    if len(arr) == 3:
        if check([blanks[arr[0]], blanks[arr[1]], blanks[arr[2]]]):
            print('YES')
            exit()
        return

    for i in range(idx, len(blanks)):
        if visited[i] == 0:
            visited[i] = 1
            combi(i+1, arr+[i])
            visited[i] = 0

combi(0, [])
print("NO")

