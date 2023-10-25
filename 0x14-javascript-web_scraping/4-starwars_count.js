#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Make a GET request to the API
request(apiUrl, function (error, response, body) {
  // Handle any errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Initialize a counter for the number of movies
  let count = 0;

  // Loop through the results array
  for (const film of data.results) {
    // Check if Wedge Antilles is in the characters array
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      // Increment the counter
      count++;
    }
  }

  // Print the counter
  console.log(count);
});
