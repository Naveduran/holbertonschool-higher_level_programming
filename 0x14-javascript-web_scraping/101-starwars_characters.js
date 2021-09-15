#!/usr/bin/node
// prints the characters present in a Star Wars Movie... same order
const request = require('request');

const movieId = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/'.concat(movieId);

request(URL, function (err, response, body) {
  if (err) { console.error(err); }
  const characters = JSON.parse(body).characters;
  for (let i = 0; characters[i]; i++) {
    request(characters[i], function (err, response, body) {
      if (err) { console.error(err); }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
