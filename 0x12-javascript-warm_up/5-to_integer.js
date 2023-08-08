#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const myNumber = Number(argv[2]);

if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNumber}`);
}
