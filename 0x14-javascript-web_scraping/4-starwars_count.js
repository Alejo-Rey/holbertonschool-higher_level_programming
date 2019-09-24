#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const title = JSON.parse(body);
  let count = 0;
  for (let x = 0; x < title.results.length; x++) {
    for (let y = 0; y < title.results[x].characters.length; y++) {
      if (title.results[x].characters[y].includes('18') === true) {
        count += 1;
      }
    }
  }
  console.log(count);
});
