import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

stack = []
count = [0] * (N + 1)
near = [0] * (N + 1)

for i in range(1, N+1):
    now = arr[i]
    if not stack:
        stack.append(i)
    else:
        while stack:
            top = arr[stack[-1]]
            if top <= now:
                stack.pop()
            else:
                break
        if stack:
            count[i] += len(stack)
            near[i] = stack[-1]
        stack.append(i)

stack = []
for i in range(N, 0, -1):
    now = arr[i]
    if not stack:
        stack.append(i)
    else:
        while stack:
            top = arr[stack[-1]]
            if top <= now:
                stack.pop()
            else:
                break
        if stack:
            count[i] += len(stack)
            r_near = stack[-1]
            if near[i] == 0:
                near[i] = r_near
            else:
                if abs(r_near - i) < abs(near[i] - i):
                    near[i] = r_near
        stack.append(i)

for i in range(1, N+1):
    if count[i] == 0:
        print(0)
        continue
    print(count[i], near[i])