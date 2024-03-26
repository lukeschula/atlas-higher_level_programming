#!/usr/bin/node

const loop = require('process');
const args = loop.argv;
const str = 'C is fun';
if (args.length >= 2) {
  for (let x = 0; x < args[2]; x++) {
    console.log(str);
  }
}
