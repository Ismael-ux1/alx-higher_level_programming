#!/usr/bin/node

exports.esrever = function (list) {
  // Initialize an empty array to store the reversed elements
  const reversed = [];

  // Iterate through the list in reverse order and add each element to the reversed array
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  // Return the reversed array
  return reversed;
};
