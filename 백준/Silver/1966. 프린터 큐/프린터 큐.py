import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    deq = deque(map(int, input().split()))
    docu = deq[M]
    # print(deq, docu)
    ans = 0
    while True:
        maximum = max(list(deq))
        a = deq.popleft()
        if a == maximum:
            ans += 1
            if M == 0:
                print(ans)
                break
            else:
                M -= 1
        else:
            deq.append(a)
            if M == 0:
                M = len(deq) - 1
            else:
                M -= 1