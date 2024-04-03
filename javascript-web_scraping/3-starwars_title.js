#!/usr/bin/noede

const episode = process.argv[2];
const Url = 'https://swapi-api.hbtn.io/api/films/' + episode;
const request = requrie('request');

request(Url, function (err, display, body) {
  if (err) {
    console.err('error:', error);
  } else {
    console.log(JAON.parse(body).title);
  }
});