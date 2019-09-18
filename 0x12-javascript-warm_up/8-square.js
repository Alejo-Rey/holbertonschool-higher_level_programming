#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
let square;
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < myVar; x++) {
    square = '';
    for (let y = 0; y < myVar; y++) {
      square += 'X';
    }
    console.log(square);
  }
}
