import sys
input = sys.stdin.readline

N = int(input())
stack = []
nums = []
for i in range(N):
    nums.append(int(input()))

i = 1
stack = []
ans = []
history = []
for n in nums:
    while not stack or stack[-1] != n:
        if i > N:
            break
        stack.append(i)
        history.append('+')
        i += 1
    else:
        s = stack.pop()
        ans.append(s)
        history.append('-')

if nums == ans:
    print(*history, sep='\n')
else:
    print("NO")