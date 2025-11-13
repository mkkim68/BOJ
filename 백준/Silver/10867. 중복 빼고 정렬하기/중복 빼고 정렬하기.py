import sys
input = sys.stdin.readline

N = int(input())
nums = set(list(map(int, input().split())))
nums = sorted(list(nums))

for i in range(len(nums)):
    print(nums[i], end=' ')