import sys
input = sys.stdin.readline


N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

s, e = 0, house[-1]
ans = 0
while s <= e:
    m = (s + e) // 2  # 거리
    last = house[0]
    cnt = 1
    for i in range(1, N):
        a = house[i]
        if a-last < m:
            continue
        elif a-last >= m:
            cnt += 1
            last = a
        if cnt > C:
            break

    if cnt >= C:
        ans = max(ans, m)
        s = m + 1
    else:
        e = m - 1
    # print('cnt', cnt, 'ans', ans)
    # print()
print(ans)
