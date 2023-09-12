#!/usr/bin/node

// Function to find the second biggest integer in an array
function findSecondLargest (numbers) {
  if (numbers.length < 2) {
    return 0; // If there are no or only one number, return 0
  }

  let largest = Math.max(...numbers);
  let secondLargest = -Infinity;

  for (const num of numbers) {
    if (num < largest && num > secondLargest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2).map(arg => parseInt(arg)); // Get and parse arguments

const secondLargest = findSecondLargest(args);

console.log(secondLargest);
