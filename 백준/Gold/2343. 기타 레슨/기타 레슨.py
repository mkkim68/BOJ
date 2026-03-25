import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minutes = list(map(int, input().split()))
max_m = max(minutes)

def check(now):
    if max_m > now:
        return False
    cnt = 1
    temp = 0
    for i in range(N):
        if temp + minutes[i] <= now:
            temp += minutes[i]
        else:
            cnt += 1
            temp = minutes[i]
        if cnt > M:
            return False
    return True

S = sum(minutes)
ans = S
s, e = S // M, S
while s <= e:
    m = (s + e) // 2
    if check(m):
        ans = min(ans, m)
        e = m - 1
    else:
        s = m + 1

print(ans)