#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (letter = 'X') {
    for (let step = 0; step < this.height; step++) {
      console.log(letter.repeat(this.width));
    }
  }
}

module.exports = Square;
