#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
function fact (myVar) {
  if (myVar <= 1) {
    return 1;
  }
  return myVar * fact(myVar - 1);
}
console.log(fact(myVar));
