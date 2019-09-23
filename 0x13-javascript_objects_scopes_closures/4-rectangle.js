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
    let x;
    let row = '';
    for (x = 0; x < this.width; x++) {
      row += 'X';
    }
    for (x = 0; x < this.height; x++) {
      console.log(row);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
