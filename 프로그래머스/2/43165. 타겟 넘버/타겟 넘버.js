function solution(numbers, target) {
    var answer = 0;
    
    const N = numbers.length;
    const queue = new Queue();
    queue.enqueue([0, numbers[0]]);
    queue.enqueue([0, -numbers[0]]);
    
    while (queue.size > 0) {
        const [idx, now] = queue.dequeue();
    
        
        if (idx === N-1) {
            if (now === target) answer++;
            continue;
        }
        
        const [n1, n2] = [now-numbers[idx+1], now+numbers[idx+1]];
        queue.enqueue([idx+1, n1]);
        queue.enqueue([idx+1, n2]);
        
    }
    return answer;
}

class Queue {
    constructor() {
        this.items = [];
        this.head = 0;
    }
    
    enqueue(x) {
        this.items.push(x);
    }
    
    dequeue(x) {
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