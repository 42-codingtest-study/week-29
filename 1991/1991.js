//문제: 1991
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = input.shift();

  const arr = {};
  const first = ["A"];
  const second = ["A"];
  const third = ["A"];

  for (let i = 0; i < n; i++) {
    let k = input[i].split(" ")[0];
    arr[k] = [input[i].split(" ")[1], input[i].split(" ")[2]];

    first.splice(first.indexOf(k) + 1, 0, ...arr[k]);
    second.splice(second.indexOf(k), 0, arr[k][0]);
    second.splice(second.indexOf(k) + 1, 0, arr[k][1]);
    third.splice(third.indexOf(k), 0, ...arr[k]);
  }
  const first1 = first.filter((e) => e != ".");
  const second1 = second.filter((e) => e != ".");
  const third1 = third.filter((e) => e != ".");
  console.log(first1.join(""));
  console.log(second1.join(""));
  console.log(third1.join(""));
}
