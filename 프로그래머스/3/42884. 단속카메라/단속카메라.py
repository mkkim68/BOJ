def solution(routes):
    answer = 0
    routes.sort()
    N = len(routes)
    
    s, e = routes[0][0], routes[0][1]
    # print(routes)
    # print(s, e)
    for i in range(1, N):
        start, end = routes[i]
        
        if start <= e:
            s = start
            e = min(e, end)
        else:
            answer += 1
            s, e = start, end
    
#         print(s, e)
    return answer+1