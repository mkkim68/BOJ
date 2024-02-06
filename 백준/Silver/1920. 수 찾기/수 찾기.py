import sys
input = sys.stdin.readline

N = int(input())
Ns = sorted(list(map(int, input().split())))
M = int(input())
Ms = list(map(int, input().split()))

def binary_search(my_list, low, high, n):
    if low > high:
        return 0
    else:
        m = (low + high) // 2
        if n > my_list[m]:
            return binary_search(my_list, m+1, high, n)
        elif n < my_list[m]:
            return binary_search(my_list, low, m-1, n)
        else:
            return 1

for i in range(M):
    num = Ms[i]
    print(binary_search(Ns, 0, N-1, num))

