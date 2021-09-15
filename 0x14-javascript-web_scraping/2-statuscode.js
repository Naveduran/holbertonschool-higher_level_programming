#!/usr/bin/node
// display the status code of a GET request
const request = require('request');

const URL = process.argv[2];
request(URL, function (response) {
  console.log('code:', response.statusCode);
});
