$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
});

$(document).ready(function() {
  $('[data-toggle=hide]').click(function() {
  	$('div.div-hide-type').slideToggle("slow");
  });
});