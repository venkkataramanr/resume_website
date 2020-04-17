jQuery(document).ready(function ($) {
    $('form').on('submit', function (event) {
        $.ajax(
            {
                data: JSON.stringify({
                    name: $('#name').val(),
                    email: $('#email').val(),
                    phone: $('#phone').val(),
                    subject: $('#subject').val(),
                    message: $('#message').val()
                }),
                type: 'POST',
                url: 'https://api.venkkatr.com'
            },
        ).done(function (data) {
            alert("Thanks for connecting. Will get in touch soon")
        });
        event.preventDefault();
    });
});