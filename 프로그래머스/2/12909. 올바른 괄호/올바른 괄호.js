function solution(s){
    var answer = true;

    let stack = [];
    
    const N = s.length
    for (i=0; i<N; i++) {
        
        if (s[i] === '(') {
            stack.push(s[i])
        } else if (s[i] === ')') {
            if (stack.length === 0) {
                answer = false
                break
            } else {
                stack.pop()
            }
        }
    }
    
    if (stack.length > 0) {
        answer = false
    }

    return answer;
}