// Select the #DIV#update_header element using jquery
$(document) .ready(function () {
    $("DIV#update_header").click(function () {
        // Update the text  of the <header> element new HEADER!!!
        $("header").text("New Header!!!");
    });
});