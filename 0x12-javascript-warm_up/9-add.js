#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const argv2 = Number(argv[2]);
const argv3 = Number(argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(argv2, argv3);
