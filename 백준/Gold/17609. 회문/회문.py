import sys
input = sys.stdin.readline

def check(s, e):
    r = e
    for l in range(s, e):
        now = string[l]
        if now == string[r]:
            r -= 1
        else:
            return False

    return True


T = int(input())
for tc in range(T):
    string = input().strip()
    N = len(string)
    j = N-1
    for i in range(N):
        s = string[i]
        if s == string[j]:
            j -= 1
            continue
        if check(i+1, j) or check(i, j-1):
            print(1)
            break
        else:
            print(2)
            break
    else:
        print(0)