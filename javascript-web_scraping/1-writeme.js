#!/usr/bin/node

const filePath = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, str, function (err) {
  if (err) throw err;
});
