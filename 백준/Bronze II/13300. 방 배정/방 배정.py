import sys
input = sys.stdin.readline

N, K = map(int, input().split())
rooms_f = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0}
rooms_m = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0}
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        rooms_f[Y] += 1
    elif S == 1:
        rooms_m[Y] += 1

ans = 0
for key in range(1, 7):
    if rooms_f[key] != 0:
        if rooms_f[key] % K == 0:
            rooms_f[key] //= K
        else:
            rooms_f[key] //= K
            rooms_f[key] += 1
        ans += rooms_f[key]
    if rooms_m[key] != 0:
        if rooms_m[key] % K == 0:
            rooms_m[key] //= K
        else:
            rooms_m[key] //= K
            rooms_m[key] += 1
        ans += rooms_m[key]

print(ans)