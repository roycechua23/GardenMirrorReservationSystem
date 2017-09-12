$(document).ready(function() {
    // JQuery code to be added in here.
    $("#events").on("change", function() {
        $("#id_package").val(2)
        
        //     $.ajax({
        //             url: '/home/retrieveEvent',
        //             data: $('#events').val().serialize(),
        //             type: 'POST',
        //             success: function(response) {
        //                 $("#id_package").val("Starter Package")
        //                 $('#memberform').trigger("reset");
        //                 $('#afterreg').modal('show');
        //             },
        //             error: function(error) {
        //                 $("#failed").toggleClass("alert-popup");
        //                 $('#memberform').trigger("reset");
        //             }
        //         });
        // });
});
