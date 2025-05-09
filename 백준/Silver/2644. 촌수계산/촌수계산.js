let filePath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
let input = require("fs").readFileSync(filePath).toString().trim().split("\n");

const N = +input.shift();
const [h1, h2] = input.shift().split(" ").map(Number);
const M = +input.shift();
const family = input.map((e) => e.split(" ").map(Number));

let edges = Array.from(Array(N + 1), () => []);

family.forEach((e) => {
  let [e1, e2] = e;
  edges[e1].push(e2);
  edges[e2].push(e1);
});

let visited = Array(N + 1).fill(false);

const dfs = (now, cnt) => {
  if (now === h2) {
    return cnt;
  }
  visited[now] = true;

  for (let next of edges[now]) {
    if (visited[next] === false) {
      const result = dfs(next, cnt + 1);
      if (result !== undefined) return result;
    }
  }
};

const answer = dfs(h1, 0);
console.log(answer !== undefined ? answer : -1);
