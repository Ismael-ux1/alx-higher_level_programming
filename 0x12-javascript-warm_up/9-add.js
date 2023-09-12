#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]); // Get the first integer argument
const arg2 = parseInt(process.argv[3]); // Get the second integer argument

if (!isNaN(arg1) && !isNaN(arg2)) {
  // Check if both arguments are valid integers
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('NaN');
}
