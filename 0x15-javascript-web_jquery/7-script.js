// fetches and lists the character names for a movie of Starwars
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('div#character').text(data.name);
  });
});
