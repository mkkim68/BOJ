import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + [1] * 10

for _ in range(1, N):
    temp = [0] * 11
    for i in range(1, 11):
        temp[i] = temp[i-1] + nums[i]
    nums = temp

print(sum(nums) % 10007)