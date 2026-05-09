function solution(maps) {
    var answer = 0;
    const [n, m] = [maps.length, maps[0].length];
    const visited = Array.from({length: n}, () => Array(m).fill(-1));
    const queue = new Queue();
    queue.enqueue([0, 0]);
    
    const deltas = [[0, 1], [1, 0], [0, -1],  [-1, 0]];
    visited[0][0] = 1
    while (queue.size > 0) {
        const cur = queue.dequeue();
        const r = cur[0], c = cur[1];
        const d = visited[r][c];
        
        
       for (let i = 0; i < 4; i++) {
            const nr = r + deltas[i][0];
            const nc = c + deltas[i][1];
            if (nr === n-1 && nc === m-1) return d+1;
            if (0<=nr && nr<n && 0<=nc && nc<m && maps[nr][nc] === 1 && visited[nr][nc] === -1) {
                visited[nr][nc] = d + 1;
                queue.enqueue([nr, nc]);
            }
        }
    }
    return visited[n-1][m-1];
}

class Queue {
    constructor() {
        this.items = [];
        this.head = 0;
    }
    
    enqueue(x) {
        this.items.push(x);
    }
    
    dequeue() {
        if (this.size === 0) return undefined;
        return this.items[this.head++];
    }
    
    front() {
        return this.items[this.head];
    }
    
    get size() {
        return this.items.length - this.head;
    }
    
    isEmpty() {
        return this.size === 0;
    }
    
}