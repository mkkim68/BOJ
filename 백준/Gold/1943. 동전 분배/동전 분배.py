import sys
input = sys.stdin.readline

for tc in range(3):
    N = int(input())
    coins = []
    total = 0
    for _ in range(N):
        coin, q = map(int, input().split())
        coins.append([coin, q])
        total += coin*q

    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    dp = [1] + [0] * total
    ans = 0
    for coin, cnt in coins:
        for t in range(total, -1, -1):
            if dp[t]:
                for k in range(1, cnt + 1):
                    if t + coin * k > total:
                        break
                    dp[t + coin * k] = 1
        if dp[-1]:
            ans = 1
            break

    print(ans)

