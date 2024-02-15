import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, *nums_a = map(int, input().split())
    b, *nums_b = map(int, input().split())
    a1, a2, a3, a4 = nums_a.count(1),nums_a.count(2),nums_a.count(3),nums_a.count(4)
    b1, b2, b3, b4 = nums_b.count(1), nums_b.count(2), nums_b.count(3), nums_b.count(4)

    if a4 > b4:
        print('A')
    elif a4 < b4:
        print('B')
    else:
        if a3 > b3:
            print('A')
        elif a3 < b3:
            print('B')
        else:
            if a2 > b2:
                print('A')
            elif a2 < b2:
                print('B')
            else:
                if a1 > b1:
                    print('A')
                elif a1 < b1:
                    print('B')
                else:
                    print('D')
