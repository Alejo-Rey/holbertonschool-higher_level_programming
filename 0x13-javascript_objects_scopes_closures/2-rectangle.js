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
}
module.exports = Rectangle;
