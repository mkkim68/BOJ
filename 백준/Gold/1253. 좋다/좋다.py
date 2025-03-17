import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

good_nums = set()
cnt = 0
for i in range(N):
    n = nums[i]

    if n in good_nums:
        cnt += 1
        continue

    l, r = 0, N-1
    while l < r:
        if l == i:
            l += 1
            continue

        if r == i:
            r -= 1
            continue

        temp = nums[l] + nums[r]
        if temp > n:
            r -= 1
        elif temp < n:
            l += 1
        else:
            cnt += 1
            good_nums.add(n)
            break

print(cnt)