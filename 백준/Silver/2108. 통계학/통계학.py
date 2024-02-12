import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = []
for n in range(N):
    nums.append(int(input()))
nums.sort()

nums_set = set(nums)
nums_freq = []
for n in nums_set:
    nums_freq.append((n, nums.count(n)))

nums_freq.sort(key=lambda x:(-x[1], x[0]))

if sum(nums) / N - sum(nums)//N >= 0.5:
    print(sum(nums)//N + 1)
else:
    print(sum(nums)//N)
print(nums[N//2])
if len(nums_freq)>1 and nums_freq[0][1] == nums_freq[1][1]:
    print(nums_freq[1][0])
else:
    print(nums_freq[0][0])
print(nums[-1]-nums[0])