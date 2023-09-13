#!/usr/bin/node
const ParentSquare = require('./5-square'); // Import the ParentSquare class

class Square extends ParentSquare {
  constructor (size) {
    super(size, size); // Call the constructor of ParentSquare with the provided size
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // Use 'X' as the default character if c is undefined
    }

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
