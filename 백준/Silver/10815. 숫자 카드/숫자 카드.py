import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Y = list(map(int, sys.stdin.readline().split()))

XnY = set(X) & set(Y)
count = [0] * M
for i in range(M):
    if Y[i] in XnY:
        count[i] = 1

print(*count)
