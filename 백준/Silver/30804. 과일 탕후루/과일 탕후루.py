import sys
input = sys.stdin.readline

N = int(input())  # 과일 갯수
fruits = list(map(int, input().split()))  # 과일 각 종류 1-9

answer = 1
info = {}
s, e, cnt = 0, 0, 0
while e < N:
    if fruits[e] not in info:
        info[fruits[e]] = 0
        cnt += 1
    info[fruits[e]] += 1
    while cnt > 2:
        info[fruits[s]] -= 1
        if info[fruits[s]] == 0:
            cnt -= 1
            del info[fruits[s]]
        s += 1

    answer = max(answer, e-s+1)
    e += 1

print(answer)
