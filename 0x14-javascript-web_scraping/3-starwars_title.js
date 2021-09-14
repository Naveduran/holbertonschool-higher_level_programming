#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer.
const request = require('request');

const movieId = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/'.concat(movieId),
  function (err, response, body) {
    if (err) { console.error(err); }
    const info = JSON.parse(body);
    console.log(info.title);
  });
