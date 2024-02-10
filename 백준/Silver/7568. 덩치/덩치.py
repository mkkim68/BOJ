import sys
input = sys.stdin.readline

N = int(input())

people_list = []
ans = []
for i in range(1, N+1):
    weight, height = map(int, input().split())
    people_list.append([weight,height])

for w, h in people_list:
    cnt = 1
    for chk_w, chk_h in people_list:
        if w < chk_w and h < chk_h:
            cnt += 1
    ans.append(cnt)

print(*ans)