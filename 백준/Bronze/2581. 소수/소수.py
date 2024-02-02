import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime_sum = 0
primes = []


for n in range(M, N+1):
    divisor = 0
    for p in range(1, n+1):
        if n % p == 0:
            divisor += 1
    if divisor == 2:
        prime_sum += n
        primes += [n]
if len(primes) != 0:
    primes.sort()
    print(prime_sum)
    print(primes[0])
else:
    print(-1)
