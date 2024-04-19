import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    command = input().strip()
    n = int(input())
    arr = input().strip()[1:-1]
    if n > 0:
        arr = deque(map(int, arr.split(',')))
    else:
        arr = deque(map(int, arr))
    # print(list(arr))
    # R: 배열 뒤집기, D 첫번째 수 버리기
    flag = 0
    for c in command:
        if c == "D" and not arr:
            print('error')
            break
        if c == "R":
            flag = (flag + 1) % 2
        elif c == "D":
            if flag == 0:
                arr.popleft()
            else:
                arr.pop()
    else:
        if flag == 0:
            print('[', end='')
            print(*arr, sep=',', end='')
            print(']')
        else:
            arr.reverse()
            print('[', end='')
            print(*arr, sep=',', end='')
            print(']')
