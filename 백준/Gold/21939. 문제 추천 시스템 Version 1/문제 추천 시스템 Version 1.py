import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

deleted = set()
def save(P, L):
    deleted.discard(P)
    problems[P] = L
    heappush(min_heap, [L, P])
    heappush(max_heap, [-L, -P])



N = int(input())
problems = {}
min_heap, max_heap = [], []
for _ in range(N):
    P, L = map(int, input().split())
    save(P, L)

M = int(input())
for _ in range(M):
    command, *arr = input().strip().split()

    if command == "recommend":
        x = int(arr[0])
        if x == 1:
            while max_heap:
                L, P = max_heap[0]
                L = -L
                P = -P
                if P in deleted or problems.get(P) != L:
                    heappop(max_heap)
                    continue
                print(P)
                break
        else:
            while min_heap:
                L, P = min_heap[0]
                if P in deleted or problems.get(P) != L:
                    heappop(min_heap)
                    continue
                print(P)
                break
    elif command == "add":
        P, L = map(int, arr)
        save(P, L)
    elif command == "solved":
        P = int(arr[0])
        del problems[P]
        deleted.add(P)

