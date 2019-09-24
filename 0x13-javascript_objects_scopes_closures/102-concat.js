#!/usr/bin/node

const fs = require('fs');
let content;

content = fs.readFileSync(process.argv[2], 'utf-8', function read (err, data) {
  if (err) {
    console.log(err);
  }
  return data;
});
fs.writeFile(process.argv[4], content, function (err) {
  if (err) {
    console.log(err);
  }
});
content = fs.readFileSync(process.argv[3], 'utf-8', function read (err, data) {
  if (err) {
    console.log(err);
  }
  content += '\n' + data;
  console.log('content2 : ' + content);
});

fs.appendFile(process.argv[4], content, function (err) {
  if (err) {
    console.log(err);
  }
});
