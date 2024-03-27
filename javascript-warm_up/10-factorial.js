#!/usr/bin/node

const { argv } = require('process');

function factor (int) {
  if (isNaN(int)) {
    int = 1;
  }
  if (int === 1) {
    return 1;
  } else {
    return int * factor(int - 1);
  }
}

const num = parseInt(argv[2]);
const display = factors(num);
console.log(display);
