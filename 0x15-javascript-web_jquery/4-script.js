// Select the DIV#toggle_header element using jQuery
$(document).ready(function () {
    $("DIV#toggle_header").click(function () {
      // Toggle the class of the <header> element between red and green
      $("header").toggleClass("red green");
    });
  });