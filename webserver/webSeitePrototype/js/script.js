
//TODO validieren username und passwort 
// url weiterleiten
 function click(){
              
 };


    function fensterOeffnen() { 
        window.open('https://qanswer-frontend.univ-st-etienne.fr/user/signup');
    }

  var btn = document.getElementById('js-qaclient-luncher');
  btn.addEventListener('click' ,getUsers, false);
  
  /*
  function getUsers(){
    var req       = new XMLHttpRequest()
        username  = ('#inputUsername').val(), 
        password  = ('#inputPassword').val();
    req.onreadystatechange = function(){
        if (req.readyState === req.DONE ){
            var result = JSON.parse(req.response);
            console.log(result);
        }
    }
    req.open('GET', 'seite.php');
    req.send();
  }
  */
