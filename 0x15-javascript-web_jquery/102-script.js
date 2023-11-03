$(document).ready(function() {
    // When the document is fully loaded, the code inside this function will run
  
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/?';
  
    // Listen for a click on the button with the ID 'btn_translate'
    $('input#btn_translate').click(function() {
      // When the button is clicked, this function will execute
  
      // Build the API URL by adding the 'lang' parameter from the input field
      const languageCode = $('input#language_code').val();
      const fullApiUrl = apiUrl + $.param({ lang: languageCode });
  
      // Send a GET request to the API and handle the response
      $.get(fullApiUrl, function(data) {
        // When the API responds, update the content of the element with the ID 'hello'
        $('div#hello').html(data.hello);
      });
    });
  });  