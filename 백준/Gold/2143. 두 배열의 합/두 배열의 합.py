import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
n = int(input())
a_nums = list(map(int, input().split()))
m = int(input())
b_nums = list(map(int, input().split()))

a_prefix = [0, a_nums[0]]
b_prefix = [0, b_nums[0]]

for i in range(2, n+1):
    a_prefix.append(a_prefix[i-1]+a_nums[i-1])

for j in range(2, m+1):
    b_prefix.append(b_prefix[j-1]+b_nums[j-1])


a_sum = []
b_sum = []

for i in range(n):
    for j in range(i+1, n+1):
        a_sum.append(a_prefix[j]-a_prefix[i])

for i in range(m):
    for j in range(i+1, m+1):
        b_sum.append(b_prefix[j]-b_prefix[i])

cnt = 0

b_sum.sort()
for a in a_sum:
    l, r = bisect_left(b_sum, T-a), bisect_right(b_sum, T-a)
    cnt += r-l

print(cnt)