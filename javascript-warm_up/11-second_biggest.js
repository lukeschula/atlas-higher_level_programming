#!/usr/bin/node

const { argv } = require('process');
let num = [];

if ((argv[2] === undefined) || (argv.length === 3)) {
  console.log(0);
} else {
  const secondBiggest = argv.slice(2);
  secondBiggest.forEach((argument) => {
    num.push(argument);
  });
  num = num.sort(function (a, b) {
    return b - a;
  });
  console.log(num[1]);
}
