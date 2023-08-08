#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const size = Number(argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let result = '';
    for (let k = 0; k < size; k++) {
      result += 'X';
    }
    console.log(result);
  }
}
