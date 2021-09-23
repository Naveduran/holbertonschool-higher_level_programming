/*
updates the text color of the <header> element to red
(#FF0000) when the user clicks on the tag DIV#red_header
*/
$(document).ready(function () {
  $('div#red_header').click(function (event) {
    $('header').css('color', '#FF0000');
  });
});
