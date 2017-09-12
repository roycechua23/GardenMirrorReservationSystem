$(document).ready(function() {
    // JQuery code to be added in here.
    $("#register").click(function () {
        
            $.ajax({
                    url: '/register',
                    data: $('#memberform').serialize(),
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
