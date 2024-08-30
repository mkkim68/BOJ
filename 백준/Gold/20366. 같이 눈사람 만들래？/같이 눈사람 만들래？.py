import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

ans = 1e9
for i in range(N-3):
    for j in range(N-1, 2, -1):
        p1, p2 = i+1, j-1
        while p1 < p2:
            temp = arr[i]+arr[j] - (arr[p1]+arr[p2])
            ans = min(ans, abs(temp))
            if temp > 0:
                p1 += 1
            else:
                p2 -= 1

print(ans)
