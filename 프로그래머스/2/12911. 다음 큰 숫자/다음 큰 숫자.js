function solution(n) {
    const C = count_one(n);
    var answer = n+1;
    
    while (true) {
        if (C === count_one(answer)) {
            break;
        }
        answer++;
    }
    
    return answer;
}
    
function count_one(n) {
    const bin_n = n.toString(2);
    const length = bin_n.length;
    let cnt = 0;
    for (let i = 0; i < length; i++) {
        if (bin_n[i] === "1") {
            cnt++;
        }
    }
    return cnt;
}