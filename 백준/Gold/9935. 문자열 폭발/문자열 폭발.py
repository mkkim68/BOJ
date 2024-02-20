import sys
input = sys.stdin.readline

string = input()[:-1]
bomb = input()[:-1]
K = len(bomb)
stack = [*string[:K-1]]

for s in range(K-1, len(string)):
    temp = string[s]
    if len(stack) >= K - 1:
        for k in range(K-1):
            a = stack.pop()
            temp += a
        if temp[::-1] != bomb:
            for t in temp[::-1]:
                stack.append(t)
    else:
        stack.append(string[s])

if stack:
    print(*stack, sep='')
else:
    print('FRULA')