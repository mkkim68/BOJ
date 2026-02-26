import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    total = sum(arr[0:M])
    if total < K:
        cnt += 1

    for i in range(1, N):
        total -= arr[i-1]
        total += arr[(i+M-1) % N]
        if i != (i+M) % N and total < K:
            cnt += 1

    print(cnt)

