#!/usr/bin/node
const Squaree = require('./5-square');
class Square extends Squaree {
  charPrint (letter = 'X') {
    super.print(letter);
  }
}

module.exports = Square;
