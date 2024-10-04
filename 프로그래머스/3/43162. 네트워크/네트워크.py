def dfs(current):
    global visited, answer
    stack = []
    stack.append(current)
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        visited[now] = 1
        for next in range(n):
            if now != next and computers[now][next]:
                stack.append(next)
    return

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            stack = []
            stack.append(i)
            while stack:
                now = stack.pop()
                if visited[now]:
                    continue
                visited[now] = 1
                for next in range(n):
                    if now != next and computers[now][next]:
                        stack.append(next)
            
    return answer