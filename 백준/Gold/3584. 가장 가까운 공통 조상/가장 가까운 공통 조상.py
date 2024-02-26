import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    par = [0] * (N+1)
    for _ in range(N-1):
        A, B = map(int, input().split())
        par[B] = A
    n1, n2 = map(int, input().split())

    par1 = []
    p1 = n1
    par1.append(p1)
    while p1:
        c = p1
        p1 = par[c]
        if p1 != 0:
            par1.append(p1)

    p2 = n2
    while p2:
        if p2 in par1:
            print(p2)
            break
        else:
            c = p2
            p2 = par[c]

