import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 수빈, 동생
visited = [0] * 100001
arr = [N]
visited[N] = 1
cnt = 0
flag = 0
time, ans = 0, 0
while flag == 0:
    temp = []
    # 뒤로 걷기
    cnt += 1
    for a in arr:
        a1 = a - 1
        a2 = a + 1
        a3 = a * 2
        if a == K:
            time = cnt-1
            ans += 1
            flag = 1
        if 0<=a1<=100000 and visited[a1] == 0:
            temp.append(a1)
        if 0<=a2<=100000 and visited[a2] == 0:
            temp.append(a2)
        if 0<=a3<=100000 and visited[a3] == 0:
            temp.append(a3)
    for p in temp:
        try:
            visited[p] = 1
        except:
            pass
    arr = temp

print(time)
print(ans)