import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
ans = []
for i in range(N):
    if not stack:
        ans.append(0)
        stack.append(i)
    else:
        while stack:
            idx = stack.pop()
            if towers[idx] >= towers[i]:
                ans.append(idx+1)
                stack.append(idx)
                break
        else:
            ans.append(0)
        stack.append(i)

print(*ans)