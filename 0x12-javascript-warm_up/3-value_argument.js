#!/usr/bin/node
// A script that prints the first argument passed to it
const [,, myArgs] = process.argv;

if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
