#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format: “ is ”
const myArgs = process.argv.slice(2);

if (myArgs.length === 2) {
  console.log(myArgs[0] + ' is ' + myArgs[1]);
} else {
  console.log('undefined is undefined');
}
