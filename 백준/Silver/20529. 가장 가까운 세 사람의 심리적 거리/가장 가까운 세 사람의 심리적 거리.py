import sys
input = sys.stdin.readline

def combination(idx, arr):
    global min_dis
    if len(arr) == 3:
        cnt = 12
        temp1, temp2, temp3 = [], [], []
        for s in arr[0]:
            temp1.append(s)
        for s in arr[1]:
            temp2.append(s)
        for s in arr[2]:
            temp3.append(s)
        cnt -= len(set(temp1) & set(temp2)) + len(set(temp1) & set(temp3)) + len(set(temp2)&set(temp3))
        min_dis = min(min_dis, cnt)
        return

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            combination(i+1, arr + [mbti[i]])
            visited[i] = 0


T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().split()
    if N > 32:
        print(0)
    else:
        min_dis = 999999
        visited = [0] * N
        combination(0, [])
        print(min_dis)