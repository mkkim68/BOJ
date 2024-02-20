import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))


prev = 0
for i in range(K):
    prev += temperature[i]
max_t = prev
for i in range(1, N-K+1):
    idx_1 = i - 1
    idx_2 = i + K - 1
    prev = prev - temperature[idx_1] + temperature[idx_2]
    if prev > max_t:
        max_t = prev

print(max_t)