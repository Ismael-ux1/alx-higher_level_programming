#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach((movie) => {
    if (movie.characters.includes(characterId)) {
      count += 1;
    }
  });
  console.log(count);
});
