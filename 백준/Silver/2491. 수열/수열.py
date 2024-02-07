import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

ans = []
to_small = to_big = 0
plus_small = plus_big = 1
if len(nums) == 1:
    ans.append(1)
else:
    for i in range(1, len(nums)):
        if to_small == 0:
            plus_small = 2
        else:
            plus_small = 1
        if to_big == 0:
            plus_big = 2
        else:
            plus_big = 1
        if nums[i-1] == nums[i]:
            to_small += plus_small
            to_big += plus_big
        elif nums[i-1] > nums[i]:
            to_small += plus_small
            ans.append(to_big)
            to_big = 0
        elif nums[i-1] < nums[i]:
            to_big += plus_big
            ans.append(to_small)
            to_small = 0
    ans += [to_big, to_small]

ans.sort()
print(ans[-1])