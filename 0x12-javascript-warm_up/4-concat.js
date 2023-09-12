#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format: “ is ”
const myArgs = process.argv.slice(2);

const arg1 = myArgs[0] || 'undefined';
const arg2 = myArgs[1] || 'undefined';

console.log(arg1 + ' is ' + arg2);
