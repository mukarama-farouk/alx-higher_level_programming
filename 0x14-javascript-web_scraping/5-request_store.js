#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
