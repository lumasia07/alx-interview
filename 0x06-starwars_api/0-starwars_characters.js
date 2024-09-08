#!/usr/bin/node

const request = require('request');

function fetchStarWarsCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching the movie:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to retrieve the movie. Status code:', response.statusCode);
      return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

fetchStarWarsCharacters(movieId);
