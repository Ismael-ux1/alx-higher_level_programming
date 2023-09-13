#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object
      return {};
    }
  }

  print () {
    // Check if width and height are valid before printing
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Swap the values of width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Double the values of width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
