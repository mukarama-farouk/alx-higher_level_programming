#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

if (!isNaN(num1) && Number.isFinite(num1) && !isNaN(num2) && Number.isFinite(num2)) {
  const results = add(num1, num2);
  console.log(results);
} else {
  console.log('NaN');
}
