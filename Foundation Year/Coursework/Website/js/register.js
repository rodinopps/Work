//Rodin Opuz
// This will run when the event page is loaded.
$(document).ready(function () {

    //This is when the form is submitted.
    $('#event-form').on('submit', function (e) {
      e.preventDefault(); //This stops the form to refresh the page after submitted.
      $('#form-messages').empty(); //This clears the form
    
      var name = $('#name').val().trim(); //This gets the name and trims any unneccessary spaces.
      var email = $('#email').val().trim(); //This gets the email and trims any unncessary spaces.

      var events = [];

      //This collects all the boxes that have been ticked.
      $("input[name='events']:checked").each(function () {
        events.push($(this).val());
      });

      //This checks if the field is empty. Whichever one.
      if (name === '' || email === '' || events.length === 0) {
        $('#form-messages').html('<p style="color:#79D4F7;">Please fill out all fields and select an event.</p>');
        return;
      }
      
      //This is what is shown when the form is completed.
      $('#form-messages').html('<p style="color:#79D4F7;">Thank you, ' + name + '! You will get updates about: ' + events.join(', ') + '.</p>');
      //Then this resets the form after a successful submission.
      $('#event-form')[0].reset();
    });
  });