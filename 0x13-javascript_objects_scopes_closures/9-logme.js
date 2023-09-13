#!/usr/bin/node
let count = 0; // Initialize a count to keep track of the number of arguments printed

exports.logMe = function (item) {
  // Print the current count and argument value
  console.log(`${count}: ${item}`);

  // Increment the count for the next call
  count++;
};
