// fetches and lists the title for all movies of Starwars
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    console.log(data);
    for (const item of data.results) {
      tittle = item.title;
      let element = "<li>" + tittle + "</li>"
      console.log(element);
      $dino2 ('ul').append(element);
    }
  });
});
