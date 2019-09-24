#!/usr/bin/node
/* function to print the new argument value */

let count = 0;

exports.logMe = function (item) {
  console.log(count++ + ': ' + item);
};
