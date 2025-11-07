import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    M, *arr = list(map(int, input().split()))
    n_dict = defaultdict(int)
    for i in range(M):
        n_dict[arr[i]] += 1

    values = list(n_dict.values())
    max_v = max(values)
    if max_v > M//2:
        for key in n_dict.keys():
            if n_dict[key] == max_v:
                print(key)
    else:
        print("SYJKGW")