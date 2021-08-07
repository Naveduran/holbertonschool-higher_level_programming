#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2], 10);

if (!parseInt(number)) {
  console.log('Missing size');
} else {
  for (let step = 0; step < number; step++) {
    console.log('X'.repeat(number));
  }
}
