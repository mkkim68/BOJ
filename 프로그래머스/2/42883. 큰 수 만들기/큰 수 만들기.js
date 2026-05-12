function solution(number, k) {
    var answer = '';
    const stack = [];
    for (let i = 0; i<number.length; i++) {
        while (stack.length > 0 && k && stack[stack.length-1] < number[i]) {
            stack.pop();
            k--;
        }
        stack.push(number[i]);
    }
    
    for (let i=0; i<stack.length-k; i++) {
        answer += stack[i];
    }
    return answer;
}