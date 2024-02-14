import sys
import math
input = sys.stdin.readline

min, max = map(int, input().split())
arr = [True for _ in range(min, max+1)]

for i in range(2, int(math.sqrt(max)+1)):
    sqr = i ** 2
    a = min // sqr
    while a*sqr <= max+1:
        if a*sqr < min:
            a += 1
            continue
        try:
            if arr[a*sqr-min]:
                arr[a*sqr-min] = False
        except:
            break
        a += 1

ans = arr.count(True)
print(ans)