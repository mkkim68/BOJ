import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A % B == 0:
        print(A)
    elif B % A == 0:
        print(B)
    else:
        A2 = A
        B2 = B
        a = 1
        i = 2
        while A > 1 and B > 1:
            if A % i != 0 or B % i != 0:
                if i >= A and i >= B:
                    break
                i += 1
                continue
            else:
                A //= i
                B //= i
                a *= i
        print(A2 * B2 // a)