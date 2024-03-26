#!/usr/bin/node

const { argv } = require('process');
const sqr = parseInt(argv[2]);
if (isNaN(sqr)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < sqr; x++) {
    for (let y = 0; y < sqr; y++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
