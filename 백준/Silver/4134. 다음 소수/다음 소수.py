import sys
import math
input = sys.stdin.readline


def isPrime(n):
    end = int(math.sqrt(n))
    if n == 0:
        return False
    elif n == 1:
        return False
    for i in range(2, end + 1):
        if n % i == 0:
            return False  # 소수가 아님
    return True


N = int(input())
for _ in range(N):
    n = int(input())
    while True:  # n보다 크거나 같은 가장 작은 소수 찾기
        ans = isPrime(n)
        if not ans:
            n += 1
        else:
            break
    print(n)