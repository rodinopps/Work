//Rodin Opuz
//This JS code only runs when the page is fully loaded.
$(document).ready(function () {

    //This is when the form is submitted.
    $('#contact-form').submit(function (e) {

        e.preventDefault(); // This stops the form from refreshing when submitted.

        //This is for the objectives in the IN0012 assignment.
        // This collects the values in the form fields and is put in variables like the other JS script.
        var name = $('#name').val(); // This stores the name value in the field from the user.
        var email = $('#email').val(); // This stores the email value in the field from the user.
        var reason = $('#reason').val(); // This stores the reason value in the field from the user.
        var message = $('#message').val(); // This stores the message value in the field from the user.

        // This will check if any of the fields are empty and if they are, it will return an error message.
        if (name === '' || email === '' || reason === '' || message === '') {
            $('#success-message').html('<p style="color:#79D4F7;">Please fill out all fields before submitting.</p>').show();
            return;
        }
        // It will essentially stop the code from running if any of the fields are empty. I learnt JS mostly from Youtube and this is something I decided to learn and use.

        // However, if all the fields are filled out, it will show the success message and will print it with the value the user entered for the name.
        $('#success-message').html('<p style="color:#79D4F7;">Thank you, ' + name + '! Your message has been sent successfully.</p>').show();
    });

});

