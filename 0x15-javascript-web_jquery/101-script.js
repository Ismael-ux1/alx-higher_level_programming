// This code uses the jQuery API to manipulate the list elements
$(document).ready(function () {
    // When the user clicks on the add_item div, a new li element is appended to the ul.my_list
    $("#add_item").click(function () {
      $("ul.my_list").append("<li>Item</li>");
    });
  
    // When the user clicks on the remove_item div, the last li element is removed from the ul.my_list
    $("#remove_item").click(function () {
      $("ul.my_list li:last").remove();
    });
  
    // When the user clicks on the clear_list div, all the li elements are removed from the ul.my_list
    $("#clear_list").click(function () {
      $("ul.my_list").empty();
    });
  });