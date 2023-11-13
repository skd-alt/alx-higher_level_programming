#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let j = 0; j < x; j++) {
    row += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(row);
  }
}
