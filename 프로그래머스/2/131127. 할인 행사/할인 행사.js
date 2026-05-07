function solution(want, number, discount) {
    var answer = 0;
    
    const count = {};
    for (let i=0; i<want.length; i++) {
        count[want[i]] = number[i];
    }
    
    const temp = {};
    for (let i = 0; i < 10; i++) {
        const fruit = discount[i];
        temp[fruit] = (temp[fruit] || 0) + 1;
    }
    let flag = true;
    let cnt = 0;
    for (const k of Object.keys(temp)) {
        if (count[k] !== temp[k]) {
            flag = false;
            break
        }
        cnt++;
    } 

    if (flag && cnt === want.length) {
        answer = 1;
    }
    for (let i = 10; i < discount.length; i++) {
        const idx = i - 10;
        const prev_fruit = discount[idx];
        if (temp[prev_fruit]) {
            temp[prev_fruit] -= 1;
            if (temp[prev_fruit] === 0) {
                delete temp[prev_fruit]
            }
        }
        const next_fruit = discount[i];
        temp[next_fruit] = (temp[next_fruit] || 0) + 1;

        let flag = true;
        let cnt = 0;
        for (const k of Object.keys(temp)) {
            if (count[k] !== temp[k]) {
                flag = false;
                break
            }
            cnt++;
        }

        if (flag && cnt === want.length) {
            answer++;
        }
    }
    

    
    return answer;
}