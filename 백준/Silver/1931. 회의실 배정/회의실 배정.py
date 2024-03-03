import sys
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))

times.sort(key=lambda x:(x[1], x[0]))
ans = [times[0]]
for i in range(1, N):
    prev = ans[-1]
    if times[i][0] >= prev[1]:
        ans.append(times[i])

print(len(ans))