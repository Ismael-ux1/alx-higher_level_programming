#!/usr/bin/node

const arg = process.argv[2]; // Get the first argument

const size = parseInt(arg); // Convert the argument to an integer

if (!isNaN(size)) {
  // Check if the conversion to integer was successful
  if (size > 0) {
    // Check if size is greater than 0
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log(''); // Print an empty line for size <= 0
  }
} else {
  console.log('Missing size');
}
