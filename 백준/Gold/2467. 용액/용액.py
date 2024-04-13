import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

s, e = 0, N-1
ans = 2e9
n1, n2 = 0, 0
while s < e:
    temp = arr[s] + arr[e]

    if abs(temp) < ans:
        ans = abs(temp)
        n1, n2 = arr[s], arr[e]

    if temp < 0:
        s += 1
    elif temp > 0:
        e -= 1
    else:
        break

print(n1, n2)