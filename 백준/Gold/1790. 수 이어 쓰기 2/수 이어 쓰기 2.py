import sys
input = sys.stdin.readline

N, k = map(int, input().split())

if k <= 9 and N >= 9:
    print(k)
else:
    # 수의 길이 구하기
    length = 0
    i = 1
    while True:
        temp = (10 ** (i-1)) * 9
        if N > temp:
            length += temp * i
            i += 1
            N -= temp
            continue
        length += i * N
        break

    if length < k:
        print(-1)
    else:
        n = 1
        now = 0
        while True:
            e = 10 ** (n-1) * 9 * n
            if now <= k < e+now:
                break
            now += e
            n += 1

        ans = str(10 ** (n-1) + (k-now-1)//n)
        print(ans[(k-now-1) % n])