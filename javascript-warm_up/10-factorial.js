#!/usr/bin/node

const { argv } = require('process');

function factors (int) {
  if (isNaN(int)) {
    int = 1;
  }
  if (int === 1) {
    return 1;
  } else {
    return int * factors(int - 1);
  }
}

const num = parseInt(argv[2]);
const display = factors(num);
console.log(display);
