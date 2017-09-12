
// $( function() {
//     $( "#event_date" ).datepicker();
//     $( "#format" ).on( "change", function() {
//       $( "#event_date" ).datepicker( "option", "dateFormat", "yyyy-mm-dd" );
//     });
//   } );
$('#event_date').datepicker();
$('#event_timestart').timepicker({'timeFormat': 'h:i A',});
$('#event_timeend').timepicker({'timeFormat': 'h:i A',});