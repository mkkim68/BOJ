function solution(n) {
    var answer = 0;
    let dp = Array(n+1).fill(0)

    dp[0] = 0
    dp[1] = 1
    
    for (let i=2; i<n+1; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    answer = dp[n]
    return answer;
}