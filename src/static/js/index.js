$(function() {
  /**
    Instead of calling the server with multiple ajax calls,
    this method takes care of it
   * @param {hash}   data sent data.
   * @param {String} method method name on the server.
   * @param {String} type type of the method.
   */
  function serverCall(data, method, type) {
    const $loading = $('#loading-spinner');

    if ($loading.css('display') === 'none') $loading.css('display', 'block');

    $.ajax({
      type: 'POST',
      url: method,
      data: JSON.stringify(data),
      contentType: 'application/json',
      dataType: 'json',
      success: function() {
        $loading.css('display', 'none');
        alert('Success Data ' + type);
      },
      error: function() {
        $loading.css('display', 'none');
        alert('something is wrong while ' + type);
      },
    });
  };

  const startProcess = function() {
    const $url = $('#url').val().replace(/\s/g, '');
    const $filename = $('#file-name').val();
    const data = [{'url': $url}, {'filename': $filename}];

    serverCall(data, 'crawler-run', 'Crawling');
    serverCall(data, 'upload-data', 'Uploading');
  };

  const accountCheck = function() {
    const $username = $('#username').val();
    const $password = $('#password').val();
    const $processLauncher = $('#js-process-launcher');
    const $loginWrapper = $('#js-login-wrapper');
    const data = [{'username': $username}, {'password': $password}];

    $.ajax({
      type: 'POST',
      url: '/check_login_data',
      data: JSON.stringify(data),
      contentType: 'application/json',
      dataType: 'json',
      success: function(e) {
        const res = e.res;
        if (res === '1') {
          $processLauncher.prop('disabled', false);
          $loginWrapper.css('display', 'none');
        }
        alert(res === '0' ? 'Error' : 'Success');
      },
      error: function() {
        alert('something is wrong, like really wrong');
      },
    });
  };

  $('#js-process-launcher').on('click', startProcess);
  $('#js-account-check').on('click', accountCheck);
});
