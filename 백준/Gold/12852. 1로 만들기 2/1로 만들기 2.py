import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
history = [0, 0]
for i in range(2, N+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i - 1], dp[i // 3], dp[i//2]) + 1
        if dp[i] == dp[i // 3] + 1:
            history.append(i // 3)
        elif dp[i] == dp[i // 2] + 1:
            history.append(i // 2)
        else:
            history.append(i - 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//3]+1)
        if dp[i-1] < dp[i//3]:
            history.append(i - 1)
        else:
            history.append(i // 3)
    elif i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//2]+1)
        if dp[i-1] < dp[i//2]:
            history.append(i - 1)
        else:
            history.append(i // 2)
    else:
        dp[i] = dp[i-1]+1
        history.append(i - 1)


ans = [N]
last = N
while True:
    if last == 1:
        break

    ans.append(history[last])
    last = history[last]

print(dp[N])
print(*ans)