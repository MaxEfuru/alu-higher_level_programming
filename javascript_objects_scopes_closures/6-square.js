#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let output = '';
        for (let j = 0; j < this.size; j++) {
          output += c;
        }
        console.log(output);
      }
    }
  }

  double () {
    super.double();
    this.size *= 2;
  }
};
