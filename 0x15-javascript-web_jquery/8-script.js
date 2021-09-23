// fetches and lists the title for all movies of Starwars
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (const item of data.results) {
      tittle = item.title;
      let element = "<li>" + tittle + "</li>"
      $('ul').append(element);
    }
  });
});
