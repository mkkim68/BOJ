import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lis = []
lis_indices = []

for i in range(N):
    num = nums[i]
    idx = bisect.bisect_left(lis, num)

    if idx == len(lis):
        lis.append(num)
        lis_indices.append(i)
    else:
        lis[idx] = num
        lis_indices[idx] = i

L = len(lis)
print(L)