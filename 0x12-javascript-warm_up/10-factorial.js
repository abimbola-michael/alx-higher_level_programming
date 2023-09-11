#!/usr/bin/node

function factorial(num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const firstArg = process.argv[2];
const argNum = parseInt(firstArg);

const result = factorial(argNum);
console.log(result);
