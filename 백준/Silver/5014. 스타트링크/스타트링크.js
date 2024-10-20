let input = require("fs").readFileSync("/dev/stdin").toString().split(" ");
let F = Number(input[0]);
let S = Number(input[1]);
let G = Number(input[2]);
let U = Number(input[3]);
let D = Number(input[4]);

class Queue {
  // 초기화
  constructor() {
    this.store = {};
    this.front = 0;
    this.rear = 0;
  }

  // 크기 구하기
  size() {
    if (this.store[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  }

  // 데이터 추가
  push(value) {
    if (this.size() === 0) {
      this.store[0] = value;
    } else {
      this.rear += 1;
      this.store[this.rear] = value;
    }
  }

  // 데이터 추출
  popleft() {
    let temp;
    if (this.front === this.rear) {
      temp = this.store[this.front];
      delete this.store[this.front];

      this.front = 0;
      this.rear = 0;
      return temp;
    } else {
      temp = this.store[this.front];
      delete this.store[this.front];
      this.front += 1;
      return temp;
    }
  }
}

let q = new Queue();
q.push(S);
let visited = new Array();
for (let i = 0; i <= F; i++) {
  visited.push(-1);
}
visited[S] = 0;
let ans = -99;

while (q.size() > 0) {
  let now = q.popleft();
  if (now === G) {
    ans = visited[now];
    break;
  }

  let up = now + U;
  let down = now - D;

  if (1 <= up && up <= F && visited[up] === -1) {
    visited[up] = visited[now] + 1;
    q.push(up);
  }
  if (1 <= down && down <= F && visited[down] === -1) {
    visited[down] = visited[now] + 1;
    q.push(down);
  }
}

if (ans === -99) {
  console.log("use the stairs");
} else {
  console.log(ans);
}
