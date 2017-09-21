$(document).ready(function() {
    // JQuery code to be added in here.
    $("#events").on("change", function() {
        // console.log($("#events").val());
        // $("#id_package").val(2);
        // $("#id_event_type").val("Birthday");
        // $("#event_date").val("2017-10-23");
        // $("#event_timestart").val("5:30 pm");
        // $("#event_timeend").val("9:30 pm");
        var event = $(this).val();
        if(event==="----------"){
            $("#id_package").val(1);
            $("#id_event_type").val("");
            $("#event_date").val("");
            $("#event_timestart").val("");
            $("#event_timeend").val("");
        }
        else{
            $.ajax({
                    url: '/home/retrieveEvent',
                    data: {
                        'event':event
                    },
                    // type: 'POST',
                    dataType:'json',
                    success: function(data) {
                       
                        console.log(data.eventtimestart)
                        console.log(data.eventtimeend)
                        $("#id_package").val(data.package);
                        $("#id_event_type").val(data.eventtype);
                        $("#event_date").val(data.eventdate);
                        $("#event_timestart").val(data.eventtimestart);
                        $("#event_timeend").val(data.eventtimeend);
                        // $("#id_package").val("Starter Package")
                        // $('#memberform').trigger("reset");
                        // $('#afterreg').modal('show');
                    },
                    error: function(error) {
                        $("#failed").toggleClass("alert-popup");
                        $('#memberform').trigger("reset");
                    }
                });
            } // closing brace for the if-else statement
        });
});
