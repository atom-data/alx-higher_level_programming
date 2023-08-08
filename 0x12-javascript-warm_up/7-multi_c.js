#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const x = Number(argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
