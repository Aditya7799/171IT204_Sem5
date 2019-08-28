var attempt = 3;
 // Variable to count number of attempts.
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

function reset_login(){

attempt=3;
document.getElementById("username").enabled = true;
document.getElementById("password").ensabled = true;
document.getElementById("submit").enabled = true;
return true;
}


function startTime()
{
var today=new Date();
var h=today.getHours();
var m=today.getMinutes();
var s=today.getSeconds();
// add a zero in front of numbers<10
m=checkTime(m);
s=checkTime(s);
document.getElementById('txt').innerHTML=h+":"+m+":"+s;
t=setTimeout('startTime()',500);
}
function checkTime(i)
{
if (i<10)
{
i="0" + i;
}
return i;
}


function check_valid_name(name)
{	
	if(name=="")
		{alert("Empty Name");
		return false;}
	
	
	return /\d/.test(name);
}

function check_valid_email(mail)
{	
	var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(mail).toLowerCase());
}

function send_question()
{

d
var name = document.getElementById("Name").value;
var email = document.getElementById("Email").value;
var subject = document.getElementById("Subject").value;
var message = document.getElementById("Message").value;

if(check_valid_name(name))
{	
	alert("Digits in name");
	return false;
}

else if(!check_valid_email(email))
{	alert("Invalid Email");
	return false;
}
else
{
	alert("We have recieved your message");

}
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