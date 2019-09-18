#!/usr/bin/node
const myVar = 'C is fun';
for (let x = 0; x < parseInt(process.argv[2]); x++) {
  console.log(myVar);
}
