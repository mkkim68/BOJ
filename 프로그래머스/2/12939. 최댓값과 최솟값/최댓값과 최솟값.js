function solution(s) {
    var answer = '';
    let temp = s.split(" ")
    temp.map((e) => parseInt(e))
    const maxnum = Math.max(...temp)
    const minnum = Math.min(...temp)
    answer = String(minnum) + ' ' + String(maxnum)
    return answer;
}