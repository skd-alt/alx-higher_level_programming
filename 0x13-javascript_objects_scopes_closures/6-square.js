#!/usr/bin/node
const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
};
