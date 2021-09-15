#!/usr/bin/node
// taks completed by a user from an api
const request = require('request');

const URL = process.argv[2];

request(URL, function (err, response, body) {
  if (err) { console.error(err); }
  const todos = JSON.parse(body);
  const usersDict = {};
  for (let todo = 0; todos[todo]; todo++) {
    if (todos[todo].completed) {
      const key = todos[todo].userId;
      if (key in usersDict) {
        usersDict[key] = usersDict[key] + 1;
      } else { usersDict[key] = 1; }
    }
  }
  console.log(usersDict);
});
