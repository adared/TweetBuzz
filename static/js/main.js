$(document).ready(function(){

	$( ".trend-name" ).click(function() {
  		$(this).parent().parent().siblings().hide( "slow");
  		$(window).scrollTop(0);
  		$(".tweet").addClass('selected-tweet');
  		$(".container").addClass('container-selected');
  		$(".trend-tweets").css("width", "100%");
  		$('.see-all').css("float", "right");
  		$('.see-all').show("slow");
	});

	$(".see-all").click(function() {
		$(".tweet").removeClass('selected-tweet');
  		$(".container").removeClass('container-selected');
  		$(".trend-tweets").css("width", "4000px");
		$(".trend").show("slow");
		$(".see-all").hide('slow');
		$(window).scrollTop(0);
		$('.see-all').css("float", "none");
	})

});

