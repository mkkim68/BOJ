def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    puddles_set = set()
    for pc, pr in puddles:
        puddles_set.add((pr-1, pc-1))
    
    dp[0][0] = 1
    for c in range(1, m):
        if (0, c) in puddles_set:
            break
        dp[0][c] = 1
    for r in range(1, n):
        if (r, 0) in puddles_set:
            break
        dp[r][0] = 1
        
    for r in range(1, n):
        for c in range(1, m):
            if (r, c) in puddles_set:
                continue
            
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[-1][-1] % 1000000007