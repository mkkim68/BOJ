import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(int(input()) for _ in range(N))

def dfs(start):
    stack = [start]
    used_idx = set()
    used_num = set()
    while stack:
        now = stack.pop()
        next = arr[now]
        used_idx.add(now)
        used_num.add(next)

        if used_idx == used_num:
            subsets.add(tuple(sorted(list(used_idx))))

        if next not in used_idx:
            stack.append(next)



subsets = set()
for i in range(1, N+1):
    dfs(i)

ans = 0
nums = []
for subset in subsets:
    ans += len(subset)
    for s in subset:
        nums.append(s)

nums.sort()
print(ans)
print(*nums, sep='\n')