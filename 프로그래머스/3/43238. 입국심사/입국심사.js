function solution(n, times) {
    var answer = 0;
    times.sort((a, b) => a-b);

    let [s, e] = [0, n*times[times.length-1]];
    
    while (s <= e) {
        const m = Math.floor((s+e)/2);
        
        let temp = 0;
        for ( const time of times ) {
            temp += Math.floor(m/time);
        }
        
        if (temp >= n) {
            answer = m;
            e = m - 1;
        } else {
            s = m + 1;
        }
        
    }
    
    return answer;
}