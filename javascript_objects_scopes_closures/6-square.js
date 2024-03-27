#!/usr/bin/node

const recallSquare = require('./5-square');

class Square extends recallSquare {
  charPrint (c) {
    const x = !c ? 'X' : c;
    for (let y = 0; y < this.height; y++) {
      console.log(x.repeat(this.width));
    }
  }
}
module.exports = Square;
