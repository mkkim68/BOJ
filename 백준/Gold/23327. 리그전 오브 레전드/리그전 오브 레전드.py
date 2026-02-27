import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix_dbl_sum = [0] * (N + 1)
prefix_dbl_sum[1] = arr[1] ** 2
prefix_sum = [0] * (N + 1)
prefix_sum[1] = arr[1]
for i in range(2, N+1):
    prefix_dbl_sum[i] = prefix_dbl_sum[i - 1] + arr[i] ** 2
    prefix_sum[i] = prefix_sum[i-1] + arr[i]


for _ in range(Q):
    l, r = map(int, input().split())
    s = prefix_sum[r]-prefix_sum[l-1]
    ans = s ** 2 - (prefix_dbl_sum[r] - prefix_dbl_sum[l-1])
    print(ans//2)