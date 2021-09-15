#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');

const URL = process.argv[2];

request(URL, function (err, response, body) {
  if (err) { console.error(err); }
  const films = JSON.parse(body);
  const character = 'https://swapi-api.hbtn.io/api/people/18/';
  let number = 0;
  for (let film = 0; film < films.count; film++) {
    if (films.results[film].characters.indexOf(character) !== -1) {
      number += 1;
    }
  }
  console.log(number);
});
