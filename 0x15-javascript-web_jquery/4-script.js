// toggles the class of the  <header> element when the user clicks on
// the tag DIV#toggle_header.
$(document).ready(function () {
  $('div#toggle_header').click(function () {
    if ($('header').hasClass('red') && $('header').hasClass('green')) {
      // It has two classes, remove one.
      $('header').removeClass('red');
    } else if ($('header').hasClass('red') || $('header').hasClass('green')) {
      // It has only one class. Toggle.
      if ($('header').hasClass('red')) {
        // It is red, toggle to green
        $('header').addClass('green');
        $('header').removeClass('red');
      } else {
        // quitar 2 y poner 1
        $('header').addClass('red');
        $('header').removeClass('green');
      }
    } else {
      // It has no class, add one
      $('header').addClass('red');
    }
  });
});
