import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int ,input().split()))
snacks.sort()

def is_possible(snack):
    cnt = 0
    for i in range(N-1, -1, -1):
        if snacks[i] >= snack:
            cnt += snacks[i] // snack
        else:
            break
        if cnt >= M:
            return True

    return False


s, e = 1, max(snacks)
ans = 0
while s <= e:
    m = (s + e) // 2
    # print(m)
    if is_possible(m):
        ans = max(ans, m)
        s = m + 1
    else:
        e = m - 1

print(ans)
