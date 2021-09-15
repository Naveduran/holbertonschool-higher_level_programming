#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filePath = process.argv[3];

request(URL, function (err, response, body) {
  if (err) { console.error(err); }
  fs.writeFile(filePath, body, 'utf8', (err, data) => {
    if (err) { console.error(err); }
  });
});
