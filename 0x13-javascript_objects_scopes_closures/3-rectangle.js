#!/usr/bin/node
/* function to export a class */
class Rectangle {
  /* class rectangle */
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    var x;
    var row = '';
    for (x = 0; x < this.width; x++) {
      row += 'X';
    }
    for (x = 0; x < this.height; x++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
