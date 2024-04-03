#!/usr/bin/node

const episode = process.argv[2];
const Url = 'https://swapi-api.hbtn.io/api/films/' + episode;
const request = require('request');

request(Url, function (error, display, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
