#!/usr/bin/node
function factorial (a) {
  return (a > 1 ? a * factorial(a - 1) : a * 1);
}

console.log(isNaN(Number(process.argv[2])) ? 1 : factorial(Number(process.argv[2])));
