// This code uses the jQuery API to get a greeting in different languages
$(document).ready(function () {
    // The url of the API service that returns the greeting
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    // When the user clicks on the translate button, a GET request is sent to the API
    $('INPUT#btn_translate').click(function () {
      // The lang parameter is set to the value of the language code input
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        // The hello div is updated with the greeting from the API response
        $('DIV#hello').html(data.hello);
      });
    });
  });