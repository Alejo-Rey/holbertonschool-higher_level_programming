#!/usr/bin/node
/* function to count the number of occurences */

exports.nbOccurences = function (list, searchElement) {
  let x; let count = 0;
  for (x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return count;
};
