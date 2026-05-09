function solution(citations) {
    var answer = citations
        .sort((a, b) => b-a)
        .filter((c, i) => c >= i+1)
        .length;
    
    return answer;
}