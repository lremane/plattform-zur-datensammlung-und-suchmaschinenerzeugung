(function() {
  var $ = jQuery;

  $.growler = function(message, options) {
    var $alert,
        css,
        offsetAmount;

    options = $.extend({}, options);
    $alert = $('<div>');
    $alert.attr('class', 'growler alert');

    if (options.type) $alert.addClass('alert-' + options.type);
    if (options.allow_dismiss)  $alert.addClass('alert-dismissible');

    $alert.append(message);

    if (options.top_offset) {
      options.offset = {
        from:   'top',
        amount: options.top_offset
      };
    }
    offsetAmount = options.offset.amount;
    $('.growler').each(function() {
      offsetAmount = Math.max(offsetAmount, parseInt($(this).css(options.offset.from)) +
                     $(this).outerHeight() + options.stackup_spacing);

      return offsetAmount;
    });

    css = {
      position:  (options.ele === 'body' ? 'fixed' : 'absolute'),
      margin:    0,
      'z-index': '9999',
      display:   'none',
      right:     '20px'
    };

    css[options.offset.from] = offsetAmount + 'px';

    $alert.css(css);

    if (options.width !== 'auto') $alert.css('width', options.width + 'px');

    $(options.ele).append($alert);

    switch (options.type) {
    case 'error':
      $alert.css('background', '#f325258c');
      break;

    case 'info':
      $alert.css('background', '#fcff448c');
      break;

    case 'success':
      $alert.css('background', '#42c16f8c');
      break;

    default:
      $alert.css('background', '#2e52d58c');
    }

    $alert.fadeIn();

    if (options.delay > 0) $alert.delay(options.delay).fadeOut();

    return $alert;
  };
}).call(this);
