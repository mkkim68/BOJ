import sys
input = sys.stdin.readline

N = int(input())
colors = []
for i in range(N):
    if i == 0:
        r, g, b = map(int, input().split())
        arr = [[r], [g], [b]]
    else:
        colors.append(list(map(int,input().split())))

for i in range(N-1):
    price = colors[i]
    temp = [[] for _ in range(3)]
    for j in range(3):
        for k in range(3):
            if j != k:
                for m in range(len(arr[j])):
                    p = price[k] + arr[j][m]
                    temp[k].append(p)
            if len(temp[k]) > 5:
                temp[k].sort()
                del temp[k][5:]
    arr = temp

ans = 1000 * 1000 + 1
for a in arr:
    for n in a:
        if n < ans:
            ans = n

print(ans)
