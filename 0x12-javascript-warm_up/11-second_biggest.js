#!/usr/bin/node

const argsList = process.argv.slice(2);
const integers = argsList.map(arg => parseInt(arg));

if (integers.length < 2) {
  console.log('0');
} else {
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
