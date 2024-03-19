import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 수빈, 동생
visited = [0] * 100001
arr = [N]
cnt = 0
flag = 0
while flag == 0:
    temp = []
    # 뒤로 걷기
    cnt += 1
    for a in arr:
        a1 = a - 1
        a2 = a + 1
        a3 = a * 2
        if a == K:
            print(cnt-1)
            flag = 1
            break
        if a1 == K or a2 == K or a3 == K:
            print(cnt)
            flag = 1
            break
        if 0<=a1<=100000 and visited[a1] == 0:
            temp.append(a1)
            visited[a1] = 1
        if 0<=a2<=100000 and visited[a2] == 0:
            temp.append(a2)
            visited[a2] = 1
        if 0<=a3<=100000 and visited[a3] == 0:
            temp.append(a3)
            visited[a3] = 1
    arr = temp


