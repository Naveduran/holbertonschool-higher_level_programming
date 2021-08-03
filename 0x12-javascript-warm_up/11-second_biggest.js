#!/usr/bin/node
const { argv } = require('process'); let biggest = argv[2]; let second = 0;

for (let step = 3; argv[step]; step++) {
  const number = parseInt(argv[step]);
  if (number > biggest) {
    second = biggest; biggest = number;
  } else if (number > second) { second = number; }
}
console.log(second);
