// adds the class red to the <header> element when the
// user clicks on the tag DIV#red_header
$(document).ready(function () {
  $('div#red_header').click(function (event) {
    $('header').addClass('red');
  });
});
