function solution(brown, yellow) {
    var answer = [];
    const total = brown + yellow
    
//     int total = brown + yellow;
//         // 가로 * 세로가 = 전체 합
//         for(int height=3;height<=total ;height++){
//             if(total%height!=0) continue;
//             int width  = total/height;            
            
//             if((width-2)*(height-2)==yellow){
//                 return new int[]{width,height};
//             }
//         }                
    
    for (let height=3; height<=total; height++) {
        if (total % height === 0) {
            let width = total / height;
            if ((width-2) * (height-2) === yellow) {
                answer.push(width, height)
                return answer;
            }
        }
    }
    return answer;
}