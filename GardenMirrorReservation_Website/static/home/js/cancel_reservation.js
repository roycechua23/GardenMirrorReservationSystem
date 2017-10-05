
$(document).ready(function() {
    $("#cancel").on("clicks", function() {
        console.log("Cancel clicked");
        var event = $(this).val();
        console.log("You selected "+event);
    });
});