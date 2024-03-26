#!/usr/bin/node

const { argv } = require('process');
const numofArgs = argv.length;
if (numofArgs <= 2) {
    console.log('No argument');
} else if (numofArgs === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
