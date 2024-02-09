import sys
input = sys.stdin.readline

stick = input()
stack = []
stick = stick.replace("()", "r")
ans = 0
for i in range(len(stick)):
    if stick[i] == "(":
        stack.append(stick[i])
        ans += 1
    elif stick[i] == "r":
        ans += len(stack)
    elif stick[i] == ")":
        stack.pop()

print(f'{ans}')