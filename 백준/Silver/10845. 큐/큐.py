import sys
input = sys.stdin.readline

N = int(input())
queue = []
command = []
for _ in range(N):
    command.append(str(input()[:-1]))

for c in command:
    if "push" in c:
        num = int(c.split(' ')[-1])
        queue.append(num)
    elif c == "back":
        if len(queue) > 0: print(queue[-1])
        else: print(-1)
    elif c == "front":
        if len(queue) > 0: print(queue[0])
        else: print(-1)
    elif c == "size":
        print(len(queue))
    elif c == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif c == "pop":
        if len(queue) > 0: print(queue.pop(0))
        else: print(-1)

