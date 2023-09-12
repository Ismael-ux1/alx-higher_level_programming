#!/usr/bin/node

const arg = process.argv[2]; // Get the first argument

const numOccurrences = parseInt(arg); // Convert the argument to an integer

if (!isNaN(numOccurrences)) {
  // Check if the conversion to integer was successful
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
