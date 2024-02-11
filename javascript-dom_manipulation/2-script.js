// changes the  color of the HTML tag HEADER to red

const $ = window.$;
$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});
