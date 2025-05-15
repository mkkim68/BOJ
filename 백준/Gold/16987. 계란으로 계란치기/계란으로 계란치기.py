import sys
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)] # 내구도, 무게
ans = 0

def dfs(depth):
    global ans

    if depth == N:
        cnt = 0
        for s, w in eggs:
            if s <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    if eggs[depth][0] <= 0:
        dfs(depth+1)
    else:
        flag = False
        for i in range(N):
            if depth != i and eggs[i][0] > 0:
                eggs[depth][0] -= eggs[i][1]
                eggs[i][0] -= eggs[depth][1]
                flag = True
                dfs(depth+1)
                eggs[depth][0] += eggs[i][1]
                eggs[i][0] += eggs[depth][1]
        if not flag:
            dfs(depth+1)

dfs(0)
print(ans)