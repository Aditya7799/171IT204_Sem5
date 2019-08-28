var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){

var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "admin" && password == "admin"){
alert ("Login successfully");
window.location = "success.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}

function send_question()
{


var name = document.getElementById("Name").value;
var email = document.getElementById("Email").value;
var subject = document.getElementById("Subject").value;
var message = document.getElementById("Message").value;

alert(name+email+subject+message);

}



function signup()
{

window.location ="signup.html";
}

function create()
{
var username = document.getElementById("username").value;
var fname = document.getElementById("Fname").value;
var lname = document.getElementById("Lname").value;
var username = document.getElementById("username").value;
var addr = document.getElementById("add").value;
var pass= document.getElementById("password").value;

if(username=="")
{
	document.getElementById("username").focus();
	return false;
}
if(fname=="")
{
	document.getElementById("Fname").focus();
	return false;
}

if(Lname=="")
{
	document.getElementById("Lname").focus();
	return false;
}

if(addr=="")
{
	document.getElementById("add").focus();
	return false;
}




}