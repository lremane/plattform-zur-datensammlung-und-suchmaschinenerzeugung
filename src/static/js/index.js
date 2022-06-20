$(function() {
  /**
    Instead of calling the server with multiple ajax calls,
    this method takes care of it
   * @param {hash}   data sent data.
   * @param {String} method method name on the server.
   * @param {String} type type of the method.
   */
  function serverCall(data, method, type) {
    var $loading = $('#loading-spinner');

    if ($loading.css('display') === 'none') $loading.css('display', 'block');

    $.ajax({
      type:        'POST',
      url:         method,
      data:        JSON.stringify(data),
      contentType: 'application/json',
      dataType:    'json',
      success:     function() {
        $loading.css('display', 'none');
        alert('Success Data ' + type);
      },
      error: function() {
        $loading.css('display', 'none');
        alert('something is wrong while ' + type);
      }
    });
  }

  var startProcess = function() {
    var $url      = $('#url').val().replace(/\s/g, ''),
        $filename = $('#file-name').val(),
        data      = [{ url: $url }, { filename: $filename }];

    serverCall(data, 'crawler-run', 'Crawling');
    serverCall(data, 'upload-data', 'Uploading');
  };

  var accountCheck = function() {
    var $username        = $('#username').val(),
        $password        = $('#password').val(),
        $processLauncher = $('#js-process-launcher'),
        $loginWrapper    = $('#js-login-wrapper'),
        data             = [{ username: $username }, { password: $password }];

    $.ajax({
      type:        'POST',
      url:         '/check_login_data',
      data:        JSON.stringify(data),
      contentType: 'application/json',
      dataType:    'json',
      success:     function(e) {
        var res = e.res;
        if (res === '1') {
          $processLauncher.prop('disabled', false);
          $loginWrapper.css('display', 'none');
        }
        alert(res === '0' ? 'Error' : 'Success');
      },
      error: function() {
        alert('something is wrong, like really wrong');
      }
    });
  };

  $('#js-process-launcher').on('click', startProcess);
  $('#js-account-check').on('click', accountCheck);
});
