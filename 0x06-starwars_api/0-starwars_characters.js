#!/usr/bin/node

const request = require("request");

// Get the Movie ID from the command-line argument
const movieId = process.argv[2];

// Define the API endpoint with the Movie ID
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const filmData = JSON.parse(body);

  // Get the array of character URLs from the response
  const characters = filmData.characters;

  // For each character URL, make an API call to get the character name
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character data and print the character name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
