let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input.shift();
const board = input.map((v) => v.split(" ").map(Number));
let maxN = 0;

for (i = 0; i < N; i++) {
  maxN = Math.max(...board[i], maxN);
}

class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
    this.tail = 0;
  }

  enqueue(value) {
    this.q[this.tail++] = value;
  }

  dequeue() {
    return this.q[this.head++];
  }

  peek() {
    return this.q[this.head];
  }

  isEmpty() {
    return this.head === this.tail;
  }

  size() {
    return this.tail - this.head;
  }
}

const dr = [0, 0, -1, 1];
const dc = [-1, 1, 0, 0];

let visited = [];
let answer = 1;

const bfs = (h, sr, sc) => {
  let q = new Queue();
  q.enqueue([sr, sc]);
  while (!q.isEmpty()) {
    let [r, c] = q.dequeue();
    if (visited[r][c]) continue;
    visited[r][c] = 1;
    for (i = 0; i < 4; i++) {
      nr = r + dr[i];
      nc = c + dc[i];
      if (
        nr >= 0 &&
        nr < N &&
        nc >= 0 &&
        nc < N &&
        board[nr][nc] > h &&
        visited[nr][nc] === 0
      ) {
        q.enqueue([nr, nc]);
      }
    }
  }
};

for (h = 1; h < maxN; h++) {
  visited = Array.from(Array(N), () => Array(N).fill(0));
  let temp = 0;
  console;
  for (r = 0; r < N; r++) {
    for (c = 0; c < N; c++) {
      if (board[r][c] > h && visited[r][c] === 0) {
        bfs(h, r, c);
        temp++;
      }
    }
  }
  answer = Math.max(answer, temp);
}

console.log(answer);
