function solution(str) {
    
    const stack = []
    
    for (let s of str) {
        if (stack.length > 0 && stack[stack.length-1] === s) {
            stack.pop()
        } else {
            stack.push(s)
        }
    }
    
    if (stack.length === 0) {
        return 1
    } else {
        return 0
    }
    
}