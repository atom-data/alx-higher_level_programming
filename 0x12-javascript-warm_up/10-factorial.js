#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const arg1 = Number(argv[2]);

function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else {
    return (factorial(n - 1) * n);
  }
}
console.log(factorial(arg1));
