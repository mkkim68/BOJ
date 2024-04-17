import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for last in range(N - 1, 0, -1):
    if A == B:
        ans = 1
        break

    m, idx = 0, 0
    for i in range(last+1):
        if A[i] > m:
            m = A[i]
            idx = i

    if last != idx:
        A[last], A[idx] = A[idx], A[last]


if A == B:
    ans = 1

print(ans)