#!/usr/bin/node

const firstArg = process.argv[2];
const size = parseInt(firstArg);
const x = 'X'

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(x.repeat(size));
  }
}
