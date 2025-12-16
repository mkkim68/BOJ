import sys
input = sys.stdin.readline

cnt = 80
is_First = True
hr = ['-'] * 80
for now in sys.stdin:
    now = now.split()
    # print(now)
    for n in now:
        if n == '<br>':
            print()
            cnt = 80
            is_First = True
        elif n == '<hr>':
            if not is_First:
                print()
            print(*hr, sep='')
            cnt = 80
            is_First = True
        else:
            L = len(n)
            if cnt + L+1 <= 80:
                print(' '+n, end='')
                cnt += (L+1)
            else:
                if is_First:
                    is_First = False
                else:
                    print()
                print(n, end='')
                cnt = L
