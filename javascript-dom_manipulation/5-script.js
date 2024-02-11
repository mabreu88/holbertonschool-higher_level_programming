/* updates the text of the HTML tag HEADER to “New Header!!!”
when the user clicks on DIV#update_header */

const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
