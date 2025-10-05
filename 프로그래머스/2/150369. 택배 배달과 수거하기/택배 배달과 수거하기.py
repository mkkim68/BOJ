def solution(cap, n, deliveries, pickups):
    answer = 0
    d_stack = [[i+1, deliveries[i]] for i in range(n) if deliveries[i] != 0]
    p_stack = [[i+1, pickups[i]] for i in range(n) if pickups[i] != 0]
    
    def stack_sol(st):
        result = 0
        max_d = 0
        while st:
            out_d = st.pop()
            if out_d[0] > max_d:
                max_d = out_d[0]
            
            if result + out_d[1] > cap:
                out_d[1] = result + out_d[1] - cap
                st.append(out_d)
                return max_d
            
            result += out_d[1]
        return max_d
    
    while d_stack or p_stack:
        answer += max(stack_sol(d_stack), stack_sol(p_stack)) * 2
        
    return answer