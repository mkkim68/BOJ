import sys
input = sys.stdin.readline

while True:
    a = input()[:-1]
    if int(a) == 0:
        break
    if a == a[::-1]:
        print('yes')
    else:
        print('no')