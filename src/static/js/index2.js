function fensterOeffnen() { 
  window.open('https://qanswer-frontend.univ-st-etienne.fr/user/signup');
}

$(function() {
    var crawlerRun = function() {
      var $url      = $('#url').val(),
          $filename = $('#filename').val(),
          $loading  = $('#loading'),
          data      = [ {"url": $url}, {"filename": $filename} ];
  
          if ($loading.css('display') === "none") $loading.css("display","block");

          $.ajax({
          type: 'POST',
          url: '/crawler-run', //upload-data
          data: JSON.stringify(data),
          contentType: 'application/json',
          dataType: 'json',
          success: function() { //fehlerbehandlung (kopieren)
            $loading.css("display","none");
            alert("Success!");
          },
          error: function() {
            $loading.css("display","none");
            alert("something is wrong");
          }
        });

        $.ajax({
          type: 'POST',
          url: 'upload-data',
          data: JSON.stringify(data),
          contentType: 'application/json',
          dataType: 'json',
          success: function() {
        $loading.css("display","none");
        alert("Success!");
      },
          error: function() {
        $loading.css("display","none");
        alert("something is wrong");
      }
      });
      };

      $('#js-crawler-luncher').on('click', crawlerRun); //start-process
  });
  