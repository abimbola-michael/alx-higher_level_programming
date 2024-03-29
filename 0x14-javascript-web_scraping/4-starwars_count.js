#!/usr/bin/node
// a script that prints the number of movies where the
// character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const charId = '18';
let count = 0;

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(charId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
