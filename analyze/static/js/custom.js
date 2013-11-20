$(document).ready(function() {
  $('.list-group a').click(function() {
  	switch(this.id){
  		case "all":
  			$(':hidden').show();
  			break;

  		case "race":
  			$('.race').show();
  			$('.practice').hide();
  			break;

		case "practice":
			$('.race').hide();
			$('.practice').show();
			break;
    }
	 $('.active').removeClass('active');
	 $(this).addClass('active');
  });


  $( "#slider" ).slider({
    disabled: true,
    range: true,
    min: 0,
    max: 100,
    values: [ 0, 100],
    slide: function( event, ui ) {
      //DO SOMETHING HERE
      //$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
    }
  });

  $(':input[data-loading-text]').click(function () {
    $(this).button('loading')  
  });

  $("#add-form #date").change(function() {
    if($(this).val() != "") {
      $("#add-form :input ").attr("disabled", false);
      $("#slider").slider("option", "disabled", false);
    }
    else {
      $("#add-form :input:not(#date)").attr("disabled", true);
      $("#slider").slider("option", "disabled", true);
    }
  });

  $('#home-menu').width($('.col-md-3').width());

  $(window).resize(function(){
    $('#home-menu').width($('.col-md-3').width());
  })
  
});