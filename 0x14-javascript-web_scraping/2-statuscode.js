#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
