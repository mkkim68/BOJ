function solution(triangle) {
    var answer = 0;
    const H = triangle.length;
//     let dp = []
    
//     for (i=0; i<H; i++) {
//         let temp = []
//         for (j=0; j<i+1; j++) {
//             temp.push(0)
//         }
//         dp.push(temp)
//     }
    
//     dp[0][0] = triangle[0][0]
    
    for (i=1; i<H; i++) {
        for (j=0; j<i+1; j++) {
            let now = triangle[i][j]
            if (j === 0) {
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            } else if (j === i) {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            } else {
                triangle[i][j] = Math.max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
            }
        }
    }

    return Math.max(...triangle[H-1]);
}