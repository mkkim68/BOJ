import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if nums[0] == nums[1]:
        print(nums[1])
    else:
        print('A')
else:
    if nums[0] == nums[1]:
        for i in range(2, N):
            if nums[i] != nums[0]:
                print('B')
                break
        else:
            print(nums[0])
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        a_temp = (nums[2] - nums[1]) / (nums[1] - nums[0])
        if a == a_temp:
            b = nums[1] - a * nums[0]

            for i in range(2, N-1):
                temp = a * nums[i] + b
                if nums[i+1] != temp:
                    print('B')
                    break
            else:
                print(a*nums[-1] + b)
        else:
            print("B")
