// A $( document ).ready() block.
$(document).ready(function () {

    $("#result").html('data2');

    $.ajax({
        url: 'https://api.acrcloud.com/v1/monitor-streams/11578/results?access_key=8cc7fd4dab415952bfddd8b47e5e7cb5&limit=5',

        type: 'GET',
        crossDomain: true,
        dataType: 'jsonp',
        success: function (data) {

            alert('jc');
            $("#result").html('data');

        },
        fail: function (jqXHR, textStatus, errorThrown) {
            alert('error');
            $("#error").html(textStatus + ': </br>' + errorThrown);
        }
    });

});
