import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

visited = [False] * 100001

cnt = 0
right = 0

for left in range(N):
    while right < N and not visited[nums[right]]:
        visited[nums[right]] = True
        right += 1

    cnt += (right - left)

    visited[nums[left]] = False

print(cnt)