#!/usr/bin/node

const fs = require('fs');
let words = '';
const args = process.argv;

words = words.concat(fs.readFileSync(args[2]));
words = words.concat(fs.readFileSync(args[3]));
fs.writeFileSync(args[4], words);
