#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not valid
      return 'Rectangle {}';
    }
  }
}

module.exports = Rectangle;
