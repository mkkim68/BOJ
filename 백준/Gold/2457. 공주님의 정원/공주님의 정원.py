import sys
input = sys.stdin.readline

N = int(input())
flowers = []
for i in range(N):
    sm, sd, em, ed = list(map(int, input().split()))
    flowers.append([sm*100 + sd, em*100 + ed])

flowers.sort()
cnt = 0
end_date = 301
while flowers:
    if end_date >= 1201 or flowers[0][0] > end_date:
        break

    temp_end_date = -1

    for _ in range(len(flowers)):
        if flowers[0][0] <= end_date:
            if temp_end_date <= flowers[0][1]:
                temp_end_date = flowers[0][1]

            flowers.remove(flowers[0])
        else:
            break

    end_date = temp_end_date
    cnt += 1

if end_date < 1201:
    print(0)
else:
    print(cnt)