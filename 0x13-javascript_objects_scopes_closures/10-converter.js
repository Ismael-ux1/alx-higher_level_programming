#!/usr/bin/node
exports.converter = function (base) {
  // Define the recursive function
  function convertToBase (n) {
    if (n < base) {
      return n.toString();
    } else {
      return convertToBase(Math.floor(n / base)) + (n % base).toString();
    }
  }

  // Return the function for converting to the specified base
  return convertToBase;
};
