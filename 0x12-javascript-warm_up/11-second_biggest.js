#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const arrayToConsider = argv.splice(2);
const sortedArray = arrayToConsider.sort((a, b) => b - a);
const length = sortedArray.length;

if (length <= 1) {
  console.log(0);
} else {
  console.log(sortedArray[1]);
}
