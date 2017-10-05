
$(document).ready(function() {
    $("#cancel").on("click", function() {
        console.log("Cancel clicked");
        var event = $(this).val();
        console.log("You selected "+event);
    });
});