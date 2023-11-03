// Use jQuery to fetch the data from the URL
$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
      // Loop through the results array and extract the title of each movie
      data.results.forEach(function (movie) {
        var title = movie.title;
        // Create a new <li> element with the title as the text
        var new_item = $("<li>" + title + "</li>");
        // Append the new <li> element to the UL#list_movies element
        $("UL#list_movies").append(new_item);
      });
    });
  });