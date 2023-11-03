// Use jQuery to fetch the data from the URL
$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
      // Extract the character name from the data
      var name = data.name;
      // Display the name in the HTML tag DIV#character
      $("DIV#character").text(name);
    });
  });