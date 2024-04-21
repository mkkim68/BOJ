import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_sorted = sorted(B)
A.sort(reverse=True)
S = 0
for i in range(N):
    S += A[i] * B_sorted[i]

print(S)