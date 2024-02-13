import sys
input = sys.stdin.readline

string = input()[:-1]
stack = []
ans = []
icp = {'(':3, '*':2, '/':2, '+': 1, '-': 1}
isp = {'(':0, '*':2, '/':2, '+': 1, '-': 1}
for s in string:  # 후위 표기법으로 변환
    if s.isalpha():
        ans.append(s)
    elif s == ')':
        while True:
            a = stack.pop()
            if a == '(':
                break
            else:
                ans.append(a)
    elif not stack or icp[s] > isp[stack[-1]]:
        stack.append(s)
    elif icp[s] <= isp[stack[-1]]:
        while True:
            if not stack or icp[s] > isp[stack[-1]]:
                stack.append(s)
                break
            else:
                a = stack.pop()
                ans.append(a)
while stack:
    ans.append(stack.pop())

print(*ans, sep='')