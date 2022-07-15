$(function() {
  var oldDataset;
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
    var $url        = $('#url'),
        $filename   = $('#file-name'),
        filenameVal = $filename.val(),
        data        = [{ url: $url.val().replace(/\s/g, '') }, { filename: filenameVal }];

    if (filenameVal !== null && filenameVal !== '') oldDataset = filenameVal;

    serverCall(data, 'process_run', 'Crawling and Uploading');
    $('#js-data-downloader').prop('disabled', false);
    $('#js-data-downloader').removeClass('disabled');

    $url.val('');
    $filename.val('');
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
    if (oldDataset === '' || oldDataset === null) {
      growler('your forgot to name your file', 'error');
    } else {
      $('a[href]').attr('href', '/data_downloader/' + oldDataset);
    }
  }

  $('#js-login-submit').on('submit', function() {
    return false;
  });

  $('#js-process-launcher').on('click', startProcess);
  $('#js-account-check').on('click', accountCheck);
  $('#js-data-downloader').on('click', dataDownloader);
});
