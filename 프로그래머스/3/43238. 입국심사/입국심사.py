def solution(n, times):
    answer = 1e9
    times.sort()
    s, e = 0, n * times[-1]

    while s <= e:
        m = (s + e) // 2 # 전체 시간
        
        temp = 0
        for time in times:
            temp += m // time
            
        if temp < n:
            s = m + 1
        else:
            answer = m
            e = m - 1
        
    return answer