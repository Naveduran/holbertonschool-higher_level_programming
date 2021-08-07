#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);

function recurse (number) {
  if (number === 0) {
    return (1);
  } return (number * recurse(number - 1));
}

if (number) {
  console.log(recurse(number));
} else {
  console.log('1');
}
