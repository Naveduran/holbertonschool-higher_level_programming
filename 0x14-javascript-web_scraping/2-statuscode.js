#!/usr/bin/node
// display the status code of a GET request
const https = require('https');

const URL = process.argv[2];
https.get(URL, function (response) {
  console.log('code:', response.statusCode);
});
