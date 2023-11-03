// Select the DIV#add_item element using jQuery
$(document).ready(function () {
    $("DIV#add_item").click(function () {
      // Create a new <li> element with the text "Item"
      var new_item = $("<li>Item</li>");
      // Append the new <li> element to the UL.my_list element
      $("UL.my_list").append(new_item);
    });
  });