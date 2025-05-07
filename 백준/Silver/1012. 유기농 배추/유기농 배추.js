let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const T = +input.shift();
const inputArr = input.map((v) => v.split(" ").map(Number));

let farm = [];
let visited = [];

const row = [0, 0, -1, 1];
const col = [1, -1, 0, 0];

const dfs = (j, k, N, M) => {
  visited[j][k] = true;
  for (let i = 0; i < 4; i++) {
    newJ = j + col[i];
    newK = k + row[i];
    if (newJ >= 0 && newJ < N && newK >= 0 && newK < M) {
      if (farm[newJ][newK] === 1 && visited[newJ][newK] === false) {
        dfs(newJ, newK, N, M);
      }
    }
  }
};

for (let i = 0; i < T; i++) {
  let answer = 0;

  let [M, N, K] = inputArr.shift();
  farm = Array.from(Array(N), () => new Array(M).fill(0));
  visited = Array.from(Array(N), () => new Array(M).fill(false));
  while (K > 0) {
    K--;
    const [x, y] = inputArr.shift();
    farm[y][x] = 1;
  }

  for (let j = 0; j < N; j++) {
    for (let k = 0; k < M; k++) {
      if (farm[j][k] === 1 && visited[j][k] === false) {
        dfs(j, k, N, M);
        answer++;
      }
    }
  }

  console.log(answer);
}
