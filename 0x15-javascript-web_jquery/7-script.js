// fetches and lists the title for all movies of Starwars
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
    const values = Object.values(data);
    for (let item = 0; values[item]; item++) {
      alert(values[item]);
      // $('div#character').append(name);
    }
  });
});
