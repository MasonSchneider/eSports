var rowCount = 0;

$('#add').click(function() {
	var email = $('#email').val();
	var summoner = $('#summoner').val();
	if(!email.length || !summoner.length) {
		$("#warning").html("Field left empty");
		$("#warning").show();
	} else if(rowCount > 5) {
		$("#warning").html("Only 5 team members allowed");
		$("#warning").show();
	} 
	//else if(email.match("@rose-hulman.edu$")!="@rose-hulman.edu") {
	//	$("#warning").html("Must have a rose-hulman email");
	//	$("#warning").show();
	//} 
	else {
		$('#team tbody').append('<tr><td>' + email +'<input type="hidden" name="' + rowCount +'email" value="' + email +'"></td>\
									<td>' + summoner + '<input type="hidden" name="' + rowCount +'summoner" value="' + summoner +'"></td></tr>');
		$("#warning").hide();
		$('#summoner').val("");
		$('#email').val("");
		rowCount++;
	}
});

$("#register").click(function() {
	if(!$('#team').val()) {
		$("#warning").html("Please enter a team name");
		$("#warning").show();
		return false;
	} else if(rowCount < 5) {
		$("#warning").html("You must have 5 members");
		$("#warning").show();
		return false;
	}
});

$(document).ready(function(){
   $("#warning").hide();
 });