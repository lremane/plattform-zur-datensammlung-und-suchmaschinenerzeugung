$(function() {
  var crawlerRun = function() {
    var $url      = $('#url').val(),
        $filename = $('#file-name').val(),
        $loading  = $('#loading'),
        data      = [ {"url": $url}, {"filename": $filename} ];

        if ($loading.css('display') === "none") $loading.css("display","block");

        $.ajax({
        type: 'POST',
        url: '/crawler-run',
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

    $('#js-crawler-luncher').on('click', crawlerRun);
});
