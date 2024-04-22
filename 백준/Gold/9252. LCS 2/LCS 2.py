import sys
from collections import deque
input = sys.stdin.readline

A = input().strip()
B = input().strip()
N, M = len(A), len(B)
LCS = [[0] * (N+1) for _ in range(M+1)]

for i in range(M+1):
    for j in range(N+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif A[j-1] == B[i-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

# for l in LCS:
#     print(l)

result = []
j, i = N, M
while i>=0 and j>=0:
    if LCS[i][j] == 0:
        break
    if LCS[i][j] == LCS[i][j-1]:
        i, j = i, j-1
    elif LCS[i][j] == LCS[i-1][j]:
        i, j = i-1, j
    else:
        result.append(B[i-1])
        i, j = i-1, j-1

result.reverse()
print(LCS[M][N])
print(*result, sep='')