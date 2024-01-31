import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
n_dict = {}
n_set = set(nums) & set(check)

for i in range(len(nums)):
    if nums[i] in n_set and nums[i] not in n_dict:
        n_dict[nums[i]] = 1
    elif nums[i] in n_set and nums[i] in n_dict:
        n_dict[nums[i]] += 1

for i in range(len(check)):
    if check[i] in n_dict:
        check[i] = n_dict[check[i]]
    else:
        check[i] = 0
        
print(*check)
