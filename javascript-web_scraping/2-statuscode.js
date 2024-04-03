#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];

request.get(Url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
