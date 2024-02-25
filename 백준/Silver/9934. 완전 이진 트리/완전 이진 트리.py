import sys
input = sys.stdin.readline


def inorder(T):
    global order
    if T:
        inorder(L[T])
        order.append(T)
        inorder(R[T])


K = int(input())
arr = list(map(int, input().split()))
L = [0] * (len(arr) + 1)
R = [0] * (len(arr) + 1)
for i in range(1, len(arr)+1):
    if i*2 <= len(arr):
        L[i] = i*2
    if i*2+1 <= len(arr):
        R[i] = i*2 + 1
ans = [0] * (len(arr) + 1)
order = []
inorder(1)

for i in range(len(arr)):
    a = order[i]
    ans[a] = arr[i]

for i in range(K):
    a = 2 ** i
    for j in range(a, 2**(i+1)):
        print(ans[j], end=' ')
    print()