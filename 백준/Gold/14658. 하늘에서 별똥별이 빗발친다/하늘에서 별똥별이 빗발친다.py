import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    r, c = map(int, input().split())
    stars.append((r, c))

ans = 0
for i in range(len(stars)):
    for j in range(len(stars)):
        cnt = 0
        for cur in range(len(stars)):
            r, c = stars[cur]
            if stars[i][0] <= r <= stars[i][0] + L and stars[j][1] <= c <= stars[j][1] + L:
                cnt += 1
        ans = max(ans, cnt)

print(K-ans)