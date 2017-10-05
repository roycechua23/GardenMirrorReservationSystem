$(document).ready(function() {
    $("#cancel").on("click", function() {
        console.log("Cancel clicked");
        var event = $('#events').val();
        console.log("You selected "+event);
        if (event === "----------"){alert("Select an event to delete first")}
        else{
            $.ajax({
                url: '/home/cancel',
                data: {
                    'event':event
                },
                type: 'POST',
                dataType:'json',
                success: function(data) {
                    console.log("Event deleted!");
                },
                error: function(error) {
                    console.log("Something went wrong.");
                    // $("#failed").toggleClass("alert-popup");
                    // $('#memberform').trigger("reset");
                }
            });
        }
        
    });
});