import sys
input = sys.stdin.readline


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)

N = int(input())

string = str(factorial(N))
ans = 0
for s in string[::-1]:
    if s == '0':
        ans += 1
    else:
        break

print(ans)