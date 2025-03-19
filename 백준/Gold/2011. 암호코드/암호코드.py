import sys
input = sys.stdin.readline

code = list(map(int, input().rstrip()))
N = len(code)

if code[0] == 0:
    print(0)
else:
    dp = [0] * (N+1)
    dp[0], dp[1] = 1, 1

    for i in range(2, N+1):
        if code[i-1] > 0:
            dp[i] += dp[i-1]
        if 10 <= code[i-2] * 10 + code[i-1] <= 26:
            dp[i] += dp[i-2]

    print(dp[N]%1000000)
