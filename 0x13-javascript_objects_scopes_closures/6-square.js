#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (letter = 'X') {
    super.print(letter);
  }
}

module.exports = Square;
