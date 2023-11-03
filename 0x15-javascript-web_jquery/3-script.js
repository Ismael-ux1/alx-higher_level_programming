// Select the DIV#red_header element using jQuery
$(document).ready(function () {
    $("DIV#red_header").click(function () {
      // Add the class red to the <header> element
      $("header").addClass("red");
    });
  });