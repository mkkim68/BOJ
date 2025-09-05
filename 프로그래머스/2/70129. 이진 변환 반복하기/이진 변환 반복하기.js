function solution(s) {
    var answer = [];
    
    function toBin(s, cnt, lev) {
        let N = 0;
        const temp = s.split("0")
        cnt += temp.length - 1
        for (const t of temp) {
            N += t.length
        }
        
        if (N === 1) {
            return [lev, cnt]
        }
        
        const newBin = N.toString(2);
        
        return toBin(newBin, cnt, lev+1)
    }
    
    answer = toBin(s, 0, 1)
    
    return answer;
}