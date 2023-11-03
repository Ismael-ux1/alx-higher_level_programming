// Select the DIV#red_header element using jQuery
$(document).ready(function () {
  $("DIV#red_header").click(function () {
    // Change the text color of the <header> element to red (#FF0000)
    $("header").css("color", "#FF0000");
  });
});
