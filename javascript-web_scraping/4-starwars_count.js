#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];
const CharaId = 18;

request(Url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(response.body).results;
    let count = 0;
    for (const film of data) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.included(`/${CharaId}/`)) {
            count++;
            break;
        }
      }
    }
    console.log(`${count}`);
  }
});