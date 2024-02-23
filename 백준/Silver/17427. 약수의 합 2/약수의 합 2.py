import sys
input = sys.stdin.readline

N = int(input())

# 에라토스테네스의 체로 소수 찾기
# 소수면 1 + 자기자신
chk = [1 for i in range(N+1)]
ans = [0,1]+[i+1 for i in range(2, N+1)]

for i in range(2, N+1):
    j = 2
    while i*j <= N:
        chk[i*j] = 0
        ans[i*j] += i
        j += 1

print(sum(ans))