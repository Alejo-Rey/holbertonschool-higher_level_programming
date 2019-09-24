#!/usr/bin/node
/* function to sort for values of the dictionary */

const list = require('./101-data').dict;

const list1 = []; const dict2 = {};

for (const x in list) {
  list1.push(x);
  dict2[list[x]] = [];
}

for (const x in list1) {
  for (const y in dict2) {
    if (list[list1[x]].toString() === y) {
      dict2[y].push(list1[x]);
    }
  }
}
console.log(dict2);
