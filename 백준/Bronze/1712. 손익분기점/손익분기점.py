import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
try:
    ans = A // (C - B)
    if ans < 0:
        print(-1)
    else:
        print(ans+1)
except:
    print(-1)
