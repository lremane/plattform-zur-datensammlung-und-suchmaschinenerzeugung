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
  alert(String(token));
  upload(token);
});

}
function test(){
  var form = new FormData();
  form.append("file", '/path/to/file/cocktails.nt');
  //alert(String(Object.values(form)))

}

/*
function upload(token){
  var form = new FormData();
  form.append("file", fileupload.files[0]);
  debugger;
  
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://qanswer-core1.univ-st-etienne.fr/api/dataset/upload?dataset=cocktails",
    "method": "POST",
    "headers": {
      "Authorization": String("Bearer "+ token),
    },
    "processData": false,
    "contentType": false,
    "mimeType": "multipart/form-data",
    "data": form
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
}
*/
