#!/usr/bin/node
// a script that writes a string to a file.

const fp = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(fp, str, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  }
});
