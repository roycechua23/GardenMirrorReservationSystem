$(document).ready(function() {
    // JQuery code to be added in here.
    $("#events").click(function () {
        
            $.ajax({
                    url: '/home/retrieveEvent',
                    data: $('#events').val().serialize(),
                    type: 'POST',
                    success: function(response) {
                        $("#success").toggleClass("alert-popup");
                        $('#memberform').trigger("reset");
                        $('#afterreg').modal('show');
                    },
                    error: function(error) {
                        $("#failed").toggleClass("alert-popup");
                        $('#memberform').trigger("reset");
                    }
                });
        });
});
