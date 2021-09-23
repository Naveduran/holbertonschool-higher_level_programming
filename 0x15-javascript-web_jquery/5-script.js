// adds a <li> element to a list when the user clicks on the
// tag DIV#add_item:
$(document).ready(function () {
  $('div#add_header').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});
