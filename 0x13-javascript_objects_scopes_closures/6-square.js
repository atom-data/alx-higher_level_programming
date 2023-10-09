#!/usr/bin/node
const SquareFirst = require('./5-square');

const Square = class extends SquareFirst {
  charPrint (c) {
    let character;
    if (c === undefined) {
      character = 'X';
    } else {
      character = c;
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        s += character;
      }
      console.log(s);
    }
  }
};
module.exports = Square;
