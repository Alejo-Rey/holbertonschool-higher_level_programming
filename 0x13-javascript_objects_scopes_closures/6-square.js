#!/usr/bin/node
const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let x;
      let row = '';
      for (x = 0; x <= this.height; x++) {
        row += c;
      }
      for (x = 0; x <= this.height; x++) {
        console.log(row);
      }
    }
  }
}
module.exports = Square;
