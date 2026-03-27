import sys
input = sys.stdin.readline

N, G, K = map(int, input().split())
infos = []

for i in range(N):
    S, L, O = map(int, input().split())
    infos.append((S, L, O))

def check(x):
    total = 0
    temp = []
    for i in range(N):
        S, L, O = infos[i]
        T = S * max(1, x-L)
        if O == 1:
            temp.append(T)
        total += T

    temp.sort(reverse=True)
    for i in range(min(len(temp), K)):
        total -= temp[i]

    return total <= G

ans = 1
s, e = 1, 2 * 10 **9
while s <= e:
    m = (s + e) // 2
    if check(m):
        s = m + 1
        ans = max(ans, m)
    else:
        e = m - 1

print(ans)
