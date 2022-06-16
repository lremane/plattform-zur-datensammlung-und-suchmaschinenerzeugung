$(function() {
  var crawlerRun = function() {
    var $url      = $('#url').val(),
        $filename = $('#file-name').val(),
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
    };

    var uploadData = function() {
        var $url      = $('#url').val(),
            $filename = $('#file-name').val(),
            $loading  = $('#loading'),
            data      = [ {"url": $url}, {"filename": $filename} ];

        if ($loading.css('display') === "none") $loading.css("display","block");


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

    var accountCheck = function() {
      var $username = $('#username').val(),
          $password = $('#password').val(),
          $processLauncher = $('#js-process-launcher'),
          $loginWrapper = $('#js-login-wrapper'),
          data      = [ {"username": $username}, {"password": $password} ];

      $.ajax({
        type: 'POST',
        url: '/check_login_data',
        data: JSON.stringify(data),
        contentType: 'application/json',
        dataType: 'json',
        success: function(e) {
          let res = e.res;
          if (res === '1') {
            $processLauncher.prop("disabled", false);
            $loginWrapper.css('visibility', 'hidden');
          }
          alert(res === '0' ? 'Error' : 'Success');
        },
        error: function() {
          alert("something is wrong, like really wrong");
        }
      });
    };

    $('#start-process').on('click', uploadData);
    $('#js-crawler-luncher').on('click', crawlerRun);
    $('#js-account-check').on('click', accountCheck);
});
