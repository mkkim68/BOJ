import bisect
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lis = []
parent = [-1] * N
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

    if idx > 0:
        parent[i] = lis_indices[idx - 1]

lis_length = len(lis)
lis_seq = [-1] * lis_length
pos = lis_indices[-1]

for i in range(lis_length-1, -1, -1):
    lis_seq[i] = nums[pos]
    pos = parent[pos]

print(lis_length)
print(*lis_seq)
