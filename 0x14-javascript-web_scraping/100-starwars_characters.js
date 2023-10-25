#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  const fetchAndPrintCharacterName = (url) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  };

  characterUrls.forEach(fetchAndPrintCharacterName);
});
