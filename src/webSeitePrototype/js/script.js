function fensterOeffnen() { 
    window.open('https://qanswer-frontend.univ-st-etienne.fr/user/signup');
}
 
//anmelden und Token zurück geben 
function getUsers(){
var data = document.getElementById("inputUsername").value,
username =data,
data = document.getElementById("inputPassword").value,
password = data;

  var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://qanswer-core1.univ-st-etienne.fr/api/user/signin",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
  },
  "processData": false,
  
  "data":  String("{\"usernameOrEmail\": \"" + username +"\", \"password\":\""+password+"\"}") 
}

$.ajax(settings).done(function (response) {
  console.log(response);
  const token = Object.values(response)[0];
  alert(token);
});
}