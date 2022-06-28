$(function() {
  function growler(msg, type) {
    $.growler(msg, {
      ele:             'body',
      type:            type,
      offset:          { from: 'top', amount: 20 },
      width:           250,
      delay:           2000,
      stackup_spacing: 1
    });

    setTimeout(function() {
      $('.growler').remove();
    }, 4000);
  }

  function serverCall(data, method, type) {
    var $loading = $('#js-loading-spinner');

    if ($loading.css('display') === 'none') $loading.css('display', 'block');

    $.ajax({
      type:        'POST',
      url:         method,
      data:        JSON.stringify(data),
      contentType: 'application/json',
      dataType:    'json',
      success:     function() {
        $loading.css('display', 'none');
        growler('Success Data ' + type, 'success');
      },
      error: function() {
        $loading.css('display', 'none');
        growler('something is wrong while ' + type, 'error');
      }
    });
  }

  var startProcess = function() {
    var $url      = $('#url').val().replace(/\s/g, ''),
        $filename = $('#file-name').val(),
        data      = [{ url: $url }, { filename: $filename }];

    serverCall(data, 'crawler-run', 'Crawling');
    serverCall(data, 'upload-data', 'Uploading');
    $('#js-data-downloader').prop('disabled', false);
    $('#js-data-downloader').removeClass('disabled');
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
        var res = e.res,
            msg = res === '0' ? 'Username, email or password is wrong' : 'Welcome!';
        if (res === '1') {
          $processLauncher.prop('disabled', false);
          $loginWrapper.animate({ height: '0px' }, 400, function() {
            $(this).remove();
          });
        }
        growler(msg, res === '0' ? 'error' : 'success');
      },
      error: function() {
        alert('something is wrong, like really wrong');
      }
    });
  };

  function dataDownloader() {
    var $filename = $('#file-name').val().replace(/\s/g, '');

    if ($filename === '') {
      growler('your forgot to name your file', 'error');
    } else {
      $('a[href]').attr('href', '/data_downloader/' + $filename);
    }
  }

  $('#js-login-submit').on('submit', function() {
    return false;
  });

  $('#js-process-launcher').on('click', startProcess);
  $('#js-account-check').on('click', accountCheck);
  $('#js-data-downloader').on('click', dataDownloader);
});
