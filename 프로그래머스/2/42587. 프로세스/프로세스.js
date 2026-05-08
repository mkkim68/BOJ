function solution(priorities, location) {
    var answer = 0;
    
    const priors = [...new Set(priorities)];
    priors.sort((a, b) => a-b);
    const count = new Map();
    
    let max_idx = priors.length-1;
    
    const queue = new Queue();

    for (const p of priorities) {
        queue.enqueue(p);
        count.set(p, (count.get(p) || 0)+ 1);
    }
    
    
    while (queue.size > 0) {
        const now = queue.dequeue();
        const p = priors[max_idx];
        if (now < p) {
            queue.enqueue(now);
            location = location > 0 ? location - 1 : queue.size - 1;
            continue;
        }
        
        const cnt = count.get(p)-1;
        if (cnt > 0) {
            count.set(p, cnt);
        } else {
            count.delete(p);
            max_idx--;
        }
        answer++;
        
        if (location === 0) {
            break;
        } else {
            location--;
        }
        
    }
    
    return answer;
}

class Queue {
    constructor() {
        this.items = [];
        this.head = 0;
    }
    
    enqueue(item) {
        this.items.push(item);
    }
    
    dequeue() {
        if (this.isEmpty()) return undefined;
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