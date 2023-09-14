#!/usr/bin/node
const fs = require('fs');
const sourceFile1 = fs.readFileSync(process.argv[2], 'utf8');
const sourceFile2 = fs.readFileSync(process.argv[3], 'utf8');
const outputFile = process.argv[4];

fs.writeFileSync(outputFile, sourceFile1 + sourceFile2);
