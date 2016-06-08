$(function() {
$('a#generate_res').bind('click', function() {
  $.getJSON('/get_res', {
    d: $('a#generate_res').attr('name')
  }, function(data) {
      $('p#captext').text('The lucky combination is:');
      $.each(data.results, function(index) {
          $('span#span_id_' + index).text(data.results[index]);
      });
    });
  return false;
});
});