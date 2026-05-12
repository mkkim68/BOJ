function solution(n,a,b)
{
    var answer = 1;
    
    let A = a;
    let B = b;

    while (true) {
        if ((A-B === 1 && B%2 === 1) || (B-A === 1 && A%2 === 1)) {
            break
        }
        A = Math.floor(A/2) + A%2;
        B = Math.floor(B/2) + B%2;
        
        answer++;
    }
    return answer;
}