#!/usr/bin/node
// A script that prints My number: <first argument converted to integer>

const arg = process.argv[2]; // Get the first argument

if (!isNaN(arg)) {
  // Check if the argument is a number
  console.log('My number:', Math.floor(arg));
} else {
  console.log('Not a number');
}
