import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

l, r = 0, N-1
ans = 1e9
while l < r:
    temp = arr[l] + arr[r]
    if abs(temp) < abs(ans):
        ans = temp

    if ans == 0:
        break

    if temp < 0:
        l += 1
    else:
        r -= 1

print(ans)