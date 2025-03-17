import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

def binary_search(target, lis):
    s, e = 0, len(lis)- 1
    while s < e:
        m = (s + e) // 2
        if lis[m] == target:
            return m
        elif lis[m-1] < target < lis[m]:
            return m
        elif target < lis[m]:
            e = m - 1
        else:
            s = m + 1
    return s

lis = [nums[0]]
for i in range(1, N):
    target = nums[i]
    if lis[-1] < target:
        lis.append(target)
    else:
        idx = binary_search(target, lis)
        lis[idx] = target


print(N - len(lis))