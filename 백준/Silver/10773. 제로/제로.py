import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    num = int(input())
    if stack and num == 0:
        stack.pop(-1)
    elif num != 0:
        stack.append(num)

if not stack:
    print(0)
else:
    print(sum(stack))