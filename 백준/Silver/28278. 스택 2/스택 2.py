import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    command = list(map(int, input().split()))

    if len(command) == 2:
        stack.append(int(command[1]))
    else:
        if command[0] == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command[0] == 3:
            print(len(stack))
        elif command[0] == 4:
            if not stack:
                print(1)
            else:
                print(0)
        elif command[0] == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)