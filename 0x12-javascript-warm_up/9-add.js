#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

const result = add(firstArg, secondArg);
console.log(result);
