#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to count the occurrences
  let count = 0;

  // Iterate through the list and count occurrences
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
