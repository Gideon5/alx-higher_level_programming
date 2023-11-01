$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const languageCode = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      success: function (data) {
        $('DIV#hello').append(data);
      },
      error: function () {
        $('DIV#hello').text('Translation not found for this language code');
      }
    });
  });
});
