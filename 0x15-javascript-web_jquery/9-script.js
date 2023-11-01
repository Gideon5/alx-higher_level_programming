const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.getJSON(url, function (body) {
  const hello = body.hello;
  $('div#hello').text(hello); // Use 'div' instead of 'DIV'
});
