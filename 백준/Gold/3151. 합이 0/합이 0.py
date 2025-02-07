import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

ans = 0
for i in range(N-1):
    l, r = i+1, N-1
    while l < r:
        left, right = arr[l], arr[r]
        temp = arr[i] + arr[l] + arr[r]
        if temp == 0:
            if arr[l] == arr[r]:
                ans += r - l
                l += 1
            else:
                rcnt, lcnt = 0, 0
                while right == arr[r]:
                    rcnt += 1
                    r -= 1
                    if right != arr[r]:
                        break

                while left == arr[l]:
                    lcnt += 1
                    l += 1
                    if left != arr[l]:
                        break

                ans += lcnt * rcnt
        elif temp > 0:
            r -= 1
        else:
            l += 1

print(ans)
