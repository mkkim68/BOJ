function solution(A,B){
    var answer = 0;
    const N = A.length;

    A.sort((a, b) => a-b)
    B.sort((a, b) => a-b)
    
    for (i=0; i<N; i++) {
        answer += A[i] * B[N-i-1]
    }

    return answer;
}