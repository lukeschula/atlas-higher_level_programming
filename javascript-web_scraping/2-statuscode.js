#1/usr/bin/Node

const request = require('request');
const Url = process.argv[2];

request.get(Url , (err, display) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${dislpy.statusCode}`);
  }

});
