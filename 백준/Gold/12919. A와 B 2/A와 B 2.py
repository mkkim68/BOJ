import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

ans = 0
def change(string):
    global ans
    if string == S:
        ans = 1
        return
    if len(string) <= len(S):
        return

    if string[0] == 'B':
        new = string[::-1]
        new.pop()
        change(new)
    if string[-1] == 'A':
        string.pop()
        change(string)

change(T)
print(ans)