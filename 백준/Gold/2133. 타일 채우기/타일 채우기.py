import sys
input = sys.stdin.readline

N = int(input())
if N%2 == 1:
    print(0)
else:
    dp = [0, 0, 3]
    for i in range(3, N+1):
        if i % 2 == 1:
            dp.append(0)
        else:
            temp = dp[i-2] * 3 + 2
            j = i - 4
            while j > 0:
                temp += dp[j] * 2
                j -= 2
            dp.append(temp)

    print(dp[N])