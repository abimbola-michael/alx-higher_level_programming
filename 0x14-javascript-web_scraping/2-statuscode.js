#!/usr/bin/node
// a script that display the status code of a GET request.

const url = process.argv[2];
const request = require('request');

request.get(url, (error, resp) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
