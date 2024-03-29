#!/usr/bin/node

// Define the factorial function using recursion
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n <= 1) {
    return 1; // Factorial of 0 and 1 is 1
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]); // Get the integer argument

const result = factorial(arg);

console.log(result);
