$(document).on('click', '#markPrinted', function () {
    // Generate URL without "id" bit

    var link = $(this).attr('data-url');
    var b = $(this);

    $.ajax({
        url: link,
        data: {
        },
        dataType: 'json',
        success: function (data) {
          if (data.status=="success") {
            b.remove();
            $('#badge'+b.attr('num')).text('Printed');
            console.log("Done :D");
          }

        }
      });
});

$(document).on('click', '#del', function () {
    // Generate URL without "id" bit

    var link = $(this).attr('data-url');
    var b = $(this);

    $.ajax({
        url: link,
        data: {
        },
        dataType: 'json',
        success: function (data) {
          if (data.status=="success") {
            b.remove();
            $('#badge'+b.attr('num')).text('Printed');
            console.log("Done :D");
          }

        }
      });
});