//문제: 1026
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = input.shift();
  const a_arr = input[0]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  const b_arr = input[1]
    .split(" ")
    .map(Number)
    .sort((a, b) => b - a);
  let answer = 0;
  for (let i = 0; i < n; i++) {
    answer += a_arr[i] * b_arr[i];
  }
  console.log(answer);
}
