#!/usr/bin/node

let iterator = 0;
exports.logMe = function (item) {
  return console.log(`${iterator++}: ${item}`);
};
