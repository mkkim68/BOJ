function solution(k, tangerine) {
    const count = new Map();
    for (const t of tangerine) {
        count.set(t, (count.get(t) || 0) + 1);
    }
    
    tangerine.sort((a, b) => count.get(b) - count.get(a) || a - b);

    let cnt = 0;
    for (let i = 0; i < k; i++) {
        const c = count.get(tangerine[i]);
        cnt += 1;
        i += c-1;
    }
    
    return cnt;
}