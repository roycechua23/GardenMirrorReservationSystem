$(document).ready(function() {

    $("#cancel").on("click", function() {
        console.log("Cancel clicked");
        var event = $('#events').val();
        console.log("You selected "+event);
        if (event === "----------"){alert("Select an event to delete first")}
        else{
            $.ajax({
                url: '/home/cancel/',
                data: {
                    'event':event
                },
                // type: 'POST',
                dataType:'json',
                success: function(data) {
                    console.log(data.message);
                    $('#deletesuccess').toggle().fadeIn(300);
                    $('#events').Find(events).remove();
                },
                error: function(error) {
                    console.log("Something went wrong.");
                    $('#deletefail').toggle().fadeIn(300);
                    // $("#failed").toggleClass("alert-popup");
                    // $('#memberform').trigger("reset");
                }
            });
        }
        
    });
    

});