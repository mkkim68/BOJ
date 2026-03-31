import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    W = input().strip()
    K = int(input())
    L = len(W)

    if K == 1:
        print(1, 1)
        continue

    char_indices = defaultdict(list)
    for i in range(L):
        char_indices[W[i]].append(i)

    min_val = float('inf')
    max_val = -1

    for char in char_indices:
        indices = char_indices[char]

        if len(indices) < K:
            continue

        for i in range(len(indices) - K + 1):
            length = indices[i+K-1] - indices[i] + 1

            min_val = min(min_val, length)
            max_val = max(max_val, length)

    if min_val == float('inf') or max_val == -1:
        print(-1)
    else:
        print(min_val, max_val)