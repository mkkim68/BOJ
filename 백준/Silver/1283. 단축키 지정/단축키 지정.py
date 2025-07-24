import sys
input = sys.stdin.readline

used = set()
words = []
idxs = []

N = int(input())

for _ in range(N):
    option = input().strip()
    words.append(option)
    temp = option.split()

    idx = 0
    flag = False
    for word in temp:
        w = word[0]
        if ord(w) in used or ord(w) + 32 in used or ord(w) - 32 in used:
            idx += len(word) + 1
            continue
        used.add(ord(w))
        idxs.append(idx)
        flag = True
        break

    if flag:
        continue

    M = len(option)
    for i in range(1, M):
        o = option[i]
        if o == ' ':
            continue
        if ord(o) in used or ord(o) + 32 in used or ord(o) - 32 in used:
            continue
        used.add(ord(o))
        idxs.append(i)
        break
    else:
        idxs.append(-1)

for i in range(N):
    if idxs[i] == -1:
        print(words[i])
    else:
        M = len(words[i])
        for j in range(M):
            if j == idxs[i]:
                print('[' + words[i][j] + ']', end='')
            else:
                print(words[i][j], end='')
        print()

# 65-90
# 97-122