import sys
input = sys.stdin.readline

stringA = '0' + input().strip()
stringB = '0' + input().strip()

N = len(stringA)
M = len(stringB)

LCS = [[0] * M for _ in range(N)]
ans = 0
# print(*LCS, sep='\n')
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif stringA[i] == stringB[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
            ans = max(ans, LCS[i][j])
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(ans)