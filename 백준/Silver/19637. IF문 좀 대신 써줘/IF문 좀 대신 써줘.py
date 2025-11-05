import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = {}
nums = []

for _ in range(N):
    name, num = input().split()
    if int(num) not in names:
        names[int(num)] = name
        nums.append(int(num))

N = len(nums)
for _ in range(M):
    now = int(input())

    s, e = 0, N-1
    while s <= e:
        m = (s + e) // 2
        if nums[m] == now:
            s = m
            break
        elif nums[m] < now:
            s = m + 1
        else:
            e = m - 1

    print(names[nums[s]])
