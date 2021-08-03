#!/usr/bin/node
const { argv } = require('process');
let a = 'undefined';
let b = 'undefined';
if (argv[2]) {
  a = argv[2];
}
if (argv[3]) {
  b = argv[3];
}
console.log(a, 'is', b);
