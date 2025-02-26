import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    costs = list(map(int, input().split()))
    stack = []
    max_cost = 0
    ans = 0
    for i in range(N-1, -1, -1):
        today = costs[i]
        max_cost = max(today, max_cost)
        if today < max_cost:
            ans += max_cost - today

    print(ans)
