import sys
from collections import deque
input = sys.stdin.readline

N =int(input())
card = deque(i for i in range(1, N+1))

# 버리고, 아래로 빼고
while len(card) > 1:
    del card[0]
    n = card.popleft()
    card.append(n)

print(*card)