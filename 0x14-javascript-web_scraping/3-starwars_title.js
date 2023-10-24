#!/usr/bin/node

const request = require('request');
const episodeId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const episodeTitle = JSON.parse(body);
    console.log(episodeTitle.title);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
