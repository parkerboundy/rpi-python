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
  
  if($("#polar").length){
   var data = [
    [0, 0],
    [30, 1],
    [45, 5],
    [90, 8],
    [150, 8.5],
    [165, 6],
    [180, 0],
    [195, 6],
    [210, 8.5],
    [270, 8],
    [330, 5],
    [0, 0]
  ]; 

    Polar("#polar", data)
  }

});



var Polar = function(element, data){

var width = 500;

  var height = 500;
  var radius = Math.min(width, height)/ 2-30;

  var r = d3.scale.linear()
      .domain([0, 10])
      .range([0, radius]);

  var line = d3.svg.line.radial()
      .radius(function(d) { return r(d[1]); })
      .angle(function(d) { 
          return (d[0])*(Math.PI/180);
      }).interpolate("cardinal");

  var svg = d3.select(element)
      .append("svg")
      .attr("height", 500)
      .attr("width", 500)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  var circles = svg.append("g")
      .attr("class", "circle axis")
      .selectAll("g")
      .data(r.ticks(4).slice(1))
      .enter().append("g");

  circles.append("circle").attr("r", r);


  circles.append("text")
      .attr("y", function(d) { return -r(d) + 10; })
      .style("text-anchor", "right")
      .text(function(d) { return d; });

  var lines = svg.append("g")
      .attr("class", "a axis")
      .selectAll("g")
      .data(d3.range(0, 360, 15))
      .enter().append("g")
      .attr("transform", function(d) { return "rotate(" + (d-90) + ")"; });

  lines.append("line")
      .attr("x2", radius);

  lines.append("text")
      .attr("x", radius + 6)
      .attr("dy", ".35em")
      .style("text-anchor", function(d) { return d < 360 && d > 180 ? "end" : null; })
      .attr("transform", function(d) { return d < 360 && d > 180 ? "rotate(180 " + (radius + 6) + ",0)" : null; })
      .text(function(d) { return d + "°"; });

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
};