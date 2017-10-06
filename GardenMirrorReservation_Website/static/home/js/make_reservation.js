$(document).ready(function() {
    $('#event_date').datepicker({format: 'yyyy-mm-dd',});
    $('#event_timestart').timepicker({'timeFormat': 'g:i a', 'scrollDefault': 'now'});
    $('#event_timeend').timepicker({'timeFormat': 'g:i a', 'scrollDefault': 'now'});
});

