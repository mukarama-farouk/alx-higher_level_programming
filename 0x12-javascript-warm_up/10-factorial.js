#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const args = process.argv[2];

const num = parseInt(args);

const results = factorial(num);

console.log(results);
