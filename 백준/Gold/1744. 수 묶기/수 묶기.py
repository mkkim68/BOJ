import sys
input = sys.stdin.readline

N = int(input())
nums_minus = []
nums_plus = []
zeros = 0
for _ in range(N):
    num = int(input())
    if num == 0:
        zeros += 1
    elif num < 0:
        nums_minus.append(num)
    else:
        nums_plus.append(num)

nums_plus.sort()
nums_minus.sort(reverse=True)
M, P = len(nums_minus), len(nums_plus)

ans = 0
if M % 2 == 1:
    if zeros == 0:
        ans += nums_minus[0]
    for i in range(1, M-1, 2):
        ans += nums_minus[i] * nums_minus[i+1]
else:
    for i in range(0, M-1, 2):
        ans += nums_minus[i] * nums_minus[i+1]

if P % 2 == 1:
    ans += nums_plus[0]
    for i in range(1, P-1, 2):
        ans += max(nums_plus[i] * nums_plus[i+1], nums_plus[i] + nums_plus[i+1])
else:
    for i in range(0, P-1, 2):
        ans += max(nums_plus[i] * nums_plus[i+1], nums_plus[i] + nums_plus[i+1])

print(ans)