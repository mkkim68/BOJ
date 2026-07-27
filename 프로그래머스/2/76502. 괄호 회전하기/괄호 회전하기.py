def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(i, n+i):
            if j >= n:
                j = j % n
            now = s[j]
            
            if stack:
                top = stack[-1]
                if now == "]" and top == "[":
                    stack.pop()
                elif now == ")" and top == "(":
                    stack.pop()
                elif now == "}" and top == "{":
                    stack.pop()
                else:
                    stack.append(now)
            else:
                stack.append(now)
        
        if not stack:
            answer += 1
                
    
    return answer