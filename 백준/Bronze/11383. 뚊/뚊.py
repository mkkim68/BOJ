import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    now = input().strip()
    temp = ''
    for n in now:
        temp += n
        temp += n
    arr.append(temp)

ans = 'Eyfa'
for i in range(N):
    now = input().strip()
    if now != arr[i]:
        ans = 'Not Eyfa'

print(ans)