#!/usr/bin/node
const list = require('./100-data').list; // Import the array from 100-data.js

console.log(list);
// Use the map method to create a new array by multiplying each value by its index
const newList = list.map((value, index) => value * index);

// Print the new list
console.log(newList);
