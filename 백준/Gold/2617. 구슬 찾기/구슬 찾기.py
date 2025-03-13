import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = {i: [set(), set()] for i in range(1, N+1)}  # 더 가벼운 것, 더 무거운 것

for _ in range(M):
    a, b = map(int, input().split())  # a가 b보다 무거움
    nums[a][0].add(b)
    nums[b][1].add(a)

stack = []
cnt = 0
for i in nums:
    for j in nums[i][0]:
        stack.append(j)
    while stack:
        now = stack.pop()
        for k in nums[now][0]:
            if k not in nums[i][0]:
                nums[i][0].add(k)
                stack.append(k)

    for j in nums[i][1]:
        stack.append(j)
    while stack:
        now = stack.pop()
        for k in nums[now][1]:
            if k not in nums[i][1]:
                nums[i][1].add(k)
                stack.append(k)

    if len(nums[i][0]) > N//2 or len(nums[i][1]) > N//2:
        cnt += 1

print(cnt)
