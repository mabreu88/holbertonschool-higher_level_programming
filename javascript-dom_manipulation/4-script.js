//  toggles the class of the HTML tag HEADER when the user clicks on the tag DIV#toggle_header

const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('red green');
});
