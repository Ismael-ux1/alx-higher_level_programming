#!/usr/bin/node
const originalDictionary = require('./101-data.js').dict;
const newDictionary = {};

for (const key in originalDictionary) {
  if (newDictionary[originalDictionary[key]]) {
    newDictionary[originalDictionary[key]].push(key);
  } else {
    newDictionary[originalDictionary[key]] = [key];
  }
}

console.log(newDictionary);
