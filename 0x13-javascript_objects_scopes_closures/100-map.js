#!/usr/bin/node
/* function to multiply an array items for its index */

const list = require('./100-data').list;

const newList = list.map(multiply);
console.log(list);
console.log(newList);
function multiply (value, index) {
  return value * index;
}
