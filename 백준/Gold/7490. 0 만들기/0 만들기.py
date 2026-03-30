import sys
input = sys.stdin.readline

arr = [' ', '+', '-']

def sol(s, now, total):
    if now == N:
        if total == 0:
            print(s)
        return

    for a in arr:
        t = s+a+str(now+1)
        t_arr = t.split('+')
        cnt = 0

        for i in range(len(t_arr)):
            temp = t_arr[i]

            if ' ' in t_arr[i]:
                temp = t_arr[i].split(' ')
                temp = ''.join(temp)
            if '-' in t_arr[i]:
                temp = temp.split('-')
                c = int(temp[0])
                for i in range(1, len(temp)):
                    c -= int(temp[i])
                temp = c

            cnt += int(temp)

        sol(t, now+1, cnt)

T = int(input())
for tc in range(T):
    if tc > 0:
        print()
    N = int(input())

    sol('1', 1, 1)
