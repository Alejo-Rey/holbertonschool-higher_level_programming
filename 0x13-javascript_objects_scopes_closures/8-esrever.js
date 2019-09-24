#!/usr/bin/node
/* function to revers a list */
exports.esrever = function (list) {
  const newList = [];
  let x;
  for (x = list.length - 1; x >= 0; x--) {
    newList.push(list[x]);
  }
  return newList;
};
