import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [0] * (N+1)
for i in range(N):
    C[A[i]] = i

for i in range(N):
    B[i] = C[B[i]]

def binary_search(target,lis):
    start,end = 0,len(lis)-1
    while start < end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]:
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

def sol(a, n):
    lis = [a[0]]
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target:
            lis.append(target)
        else:
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis)

print(sol(B, N))

