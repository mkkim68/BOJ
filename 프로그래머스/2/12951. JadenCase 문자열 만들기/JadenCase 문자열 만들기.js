function solution(s) {
    var answer = '';
    const arr = s.split(" ");
    console.log(arr)
    for (const word of arr) {
        console.log(word)
        const N = word.length;
        for (i=0; i<N; i++) {
            if (i===0){
                if (word[i] >= 'a' && word[i] <= 'z') {
                    answer += word[0].toUpperCase()
                } else {
                    answer += word[0]
                }
            } else {
                if (word[i] >= 'A' && word[i] <= 'Z') {
                    answer += word[i].toLowerCase()
                } else {
                    answer += word[i]
                }
            }
        }
        answer += ' '
    }
    return answer.slice(0, -1);
}