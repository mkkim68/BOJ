import sys
input = sys.stdin.readline

N, K, P, X = map(int, input().split())
nums = {
    0: '0b1111110',
    1: '0b0000110',
    2: '0b1011011',
    3: '0b1001111',
    4: '0b0100111',
    5: '0b1101101',
    6: '0b1111101',
    7: '0b1000110',
    8: '0b1111111',
    9: '0b1101111'
}

strX = list(str(X).zfill(K))

changes = {}
for x in set(strX):
    ix = int(x)
    changes[ix] = []
    for y in range(10):
        c = int(nums[y], 2) ^ int(nums[ix], 2)
        changes[ix].append(bin(c).count('1'))

used = set()

def sol(idx, current_n, left):
    if idx == K:
        if 1 <= current_n <= N and current_n != X:
            used.add(current_n)
        return

    now = int(strX[idx])
    for i in range(10):
        diff = changes[now][i]
        if diff <= left:
            sol(idx + 1, current_n * 10 + i, left - diff)

sol(0, 0, P)

print(len(used))