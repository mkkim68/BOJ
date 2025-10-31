import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

books.sort()

minus, plus = [], []
for book in books:
    if book < 0:
        minus.append(book)
    else:
        plus.append(book)

ans = 0
if minus and plus:
    if -minus[0] > plus[-1]:
        for i in range(0, len(minus), M):
            if i == 0:
                ans += -minus[i]
            else:
                ans += -minus[i] * 2

        for i in range(len(plus)-1, -1, -M):
            ans += plus[i] * 2
    else:
        for i in range(0, len(minus), M):
            ans += -minus[i] * 2

        for i in range(len(plus) - 1, -1, -M):
            if i == len(plus) - 1:
                ans += plus[i]
            else:
                ans += plus[i] * 2
elif minus:
    for i in range(0, len(minus), M):
        if i == 0:
            ans += -minus[i]
        else:
            ans += -minus[i] * 2
elif plus:
    for i in range(len(plus) - 1, -1, -M):
        if i == len(plus) - 1:
            ans += plus[i]
        else:
            ans += plus[i] * 2

print(ans)