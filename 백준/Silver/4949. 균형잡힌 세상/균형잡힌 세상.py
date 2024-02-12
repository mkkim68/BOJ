import sys
input = sys.stdin.readline


while True:
    stack = []
    string = input()[:-1]
    if string == '.':
        break
    for s in string:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop(-1)
        elif s == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop(-1)
    else:
        if not stack:
            print('yes')
        else:
            print('no')
        

