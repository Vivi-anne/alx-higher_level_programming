#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

/*
 *@property {method} print - prints the rectangle using the character X
 */
  print () {
    for (let i = 0; i < this.height; i++) {
      let sRow = '';
      for (let j = 0; j < this.width; j++) {
        sRow += 'X';
      }
      console.log(sRow);
    }
  }
}

module.exports = Rectangle;
