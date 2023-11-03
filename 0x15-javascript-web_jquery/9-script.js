// Use jQuery to fetch the data from the URL
$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
      // Extract the value of hello from the data
      var hello = data.hello;
      // Display the value of hello in the HTML tag DIV#hello
      $("DIV#hello").text(hello);
    });
  });