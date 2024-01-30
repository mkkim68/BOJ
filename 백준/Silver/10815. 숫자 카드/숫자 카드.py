import sys
input = sys.stdin.readline

N = int(input())
X = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Y = list(map(int, sys.stdin.readline().split()))

count = [0] * M
for i in range(M):
    if Y[i] in X:
        count[i] = 1

print(*count)
