import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 1e9
now_sum = 0
end = 0
for i in range(N):
    while now_sum < S:
        if end >= N:
            break
        now_sum += arr[end]
        end += 1
    else:
        ans = min(ans, end-i)
    now_sum -= arr[i]

if ans < 1e9:
    print(ans)
else:
    print(0)