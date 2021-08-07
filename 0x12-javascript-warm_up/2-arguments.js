#!/usr/bin/node
const { argv } = require('process');

let myVar = '';
if (!argv[2]) {
  myVar = 'No argument';
}
if (argv[2] && !argv[3]) {
  myVar = 'Argument found';
}
if (argv[2] && argv[3]) {
  myVar = 'Arguments found';
}
console.log(myVar);
