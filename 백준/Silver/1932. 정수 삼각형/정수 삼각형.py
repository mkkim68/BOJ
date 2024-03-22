import sys
input = sys.stdin.readline

N = int(input())
p = []
for i in range(1, N+1):
    cur = list(map(int, input().split()))
    if p:
        temp = [0] * i
        for idx in range(i):
            if idx == 0:
                temp[idx] = p[idx] + cur[idx]
            elif idx == i-1:
                temp[idx] = p[idx-1] + cur[idx]
            else:
                temp[idx] = max(p[idx-1] + cur[idx], p[idx]+cur[idx])
        p = temp
    else:
        p = cur

print(max(p))