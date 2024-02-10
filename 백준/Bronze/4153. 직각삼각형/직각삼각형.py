import sys
input = sys.stdin.readline

while True:
    a, b, c = list(map(int, input().split()))
    nums = sorted([a, b, c])
    if a == b == c == 0:
        break
    if nums[2] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print('right')
    else:
        print('wrong')