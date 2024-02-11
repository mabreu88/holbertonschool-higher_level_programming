/*  fetches and lists the title for all movies by using this
URL: https://swapi-api.hbtn.io/api/films/?format=json */

// get(): Load data from the server using a HTTP GET request.

// https://api.jquery.com/jquery.get/

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movies in data.results) {
    $('ul#list_movies').append('<li>' + data.results[movies].title + '</li>');
  }
});
