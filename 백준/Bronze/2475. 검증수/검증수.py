import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
ans = 0
for n in nums:
    ans += n ** 2

print(ans % 10)