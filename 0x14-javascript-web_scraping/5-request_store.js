#!/usr/bin/node
// a script that gets the contents of a webpage and stores
// it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fp = process.argv[3];

request(url).pipe(fs.createWriteStream(fp));
