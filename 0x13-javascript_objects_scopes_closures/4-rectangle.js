#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (letter = 'X') {
    for (let step = 0; step < this.height; step++) {
      console.log(letter.repeat(this.width));
    }
  }

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
