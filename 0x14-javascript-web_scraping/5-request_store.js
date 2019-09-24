#!/usr/bin/node

const req = require('request');
const fs = require('fs');
let content;

req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    content = body;
  }
  fs.writeFile(process.argv[3], content, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
