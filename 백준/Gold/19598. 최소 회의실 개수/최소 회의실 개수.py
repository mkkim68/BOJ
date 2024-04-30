import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split())))

arr.sort()
# print(arr)
stack = []
for s, e in arr:
    # stack.sort(key=lambda x: abs(s-x))
    if not stack:
        stack.append(e)
    else:
        for idx in range(len(stack)):
            if stack[idx] <= s:
                stack[idx] = e
                break
        else:
            stack.append(e)

print(len(stack))
