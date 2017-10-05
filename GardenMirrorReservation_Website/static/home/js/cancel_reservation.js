
$(document).ready(function() {
    $("#cancel").on("click", function() {
        console.log("Cancel clicked");
        var event = $('#events').val();
        console.log("You selected "+event);
    });
});