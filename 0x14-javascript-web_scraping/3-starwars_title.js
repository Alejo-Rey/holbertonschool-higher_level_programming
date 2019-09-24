#!/usr/bin/node

const req = require('request');

req('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const title = JSON.parse(body);
  console.log(title.title);
});
