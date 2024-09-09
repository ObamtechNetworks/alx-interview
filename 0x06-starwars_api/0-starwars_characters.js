#!/usr/bin/node
const request = require("request");
const ID = process.argv[2];

if (!ID) {
  console.log("Error: Missing movie ID argument.");
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${ID}/`;

function getCharacter(listChar, index) {
  if (!Array.isArray(listChar)) {
    console.log("Error: 'listChar' is not an array.");
    return;
  }

  if (index === listChar.length) {
    return;
  }

  request(`${listChar[index]}`, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const character = JSON.parse(response.body);
      console.log(character.name);
      getCharacter(listChar, index + 1);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(response.body);
    const listChar = film.characters;

    if (Array.isArray(listChar)) {
      getCharacter(listChar, 0);
    } else {
      console.log("Error: 'characters' is not an array or is undefined.");
    }
  }
});
