#!/usr/bin/node

const Url =process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs =require('fs');

request(Url, function (error, response, body) {
  if (error) {
    console.error('error:' error);
  } else {
    fs.writeFile(filePath, body, function (err) {
      if (err) throw err;
    });
  }
});

