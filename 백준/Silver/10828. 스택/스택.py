import sys
input = sys.stdin.readline

N = int(input())
stack = []
command = []
for _ in range(N):
    command.append(str(input()[:-1]))

for c in command:
    if "push" in c:
        num = int(c.split(' ')[-1])
        stack.append(num)
    elif c == "top":
        if len(stack) > 0: print(stack[-1])
        else: print(-1)
    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    elif c == "pop":
        if len(stack) > 0: print(stack.pop(-1))
        else: print(-1)

