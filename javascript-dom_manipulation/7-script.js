//  fetches the name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

// get(): Load data from the server using a HTTP GET request.

// https://api.jquery.com/jquery.get/

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('div#character').html(data.name);
});
