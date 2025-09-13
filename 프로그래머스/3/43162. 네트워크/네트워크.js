function solution(n, computers) {
    var answer = 0;
    
    let visited = new Array(n).fill(0)
    
    // console.log(visited)
    
    for (i=0; i<n; i++) {
        if (visited[i]) continue;
        
        answer += 1;
        let stack = [i];
        while (stack.length) {
            let now = stack.pop();
            visited[now] = 1
            
            for (j=0; j<n; j++) {
                if (now != j && computers[now][j] && !visited[j]) {
                    stack.push(j)
                }
            }
        }
    }
    
    return answer;
}