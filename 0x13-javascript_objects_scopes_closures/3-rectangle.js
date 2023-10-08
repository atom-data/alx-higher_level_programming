#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += 'X';
      }
      console.log(s);
    }
  }
};
module.exports = Rectangle;
