let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const nums = input[1].split(" ").map(Number);

const deque = [];
for (i = 1; i <= N; i++) {
  deque.push(i);
}

let answer = 0;

nums.forEach((num) => {
  while (true) {
    if (deque[0] === num) {
      deque.shift();
      break;
    } else if (deque.indexOf(num) <= deque.length / 2) {
      let temp = deque[0];
      deque.shift();
      deque.push(temp);
      answer += 1;
    } else if (deque.indexOf(num) > deque.length / 2) {
      let temp = deque[deque.length - 1];
      deque.pop();
      deque.unshift(temp);
      answer += 1;
    }
  }
});

console.log(answer);
