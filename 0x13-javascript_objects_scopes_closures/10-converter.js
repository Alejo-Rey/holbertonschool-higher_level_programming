#!/usr/bin/node
/* function to convert to any base */

exports.converter = function (base) {
  return function (name) {
    return name.toString(base);
  };
};
