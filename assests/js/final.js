$(document).ready(function() {
	$(window).scroll(function () {
		if ($(window).scrollTop() > 200) {
			$('#top').fadeIn();
		} else {
			$('#top').fadeOut();
		}
		});
		$('#top').click(function () {
			$('HTML').animate({scrollTop: 0}, 1000);
	});

	setTimeout(function(){
        $('#message').fadeOut('slow');
    }, 4000);

    AOS.init({
    	duration:600,
    	once:true,
	});
	$(window).scroll(function(){
		if($(window).scrollTop()>500)
		{
			$('.navbar').addClass('black');
		}
		else
		{
			$('.navbar').removeClass('black');
		}
	});
	var headerHeight= $('header').outerHeight();
	console.log(headerHeight);
	$(document).ready(function(){
		$('.scroll').on('click', function(e) {
     	e.preventDefault();
     	var target = $(this).attr('href');
     	$('html, body').animate({
       	scrollTop: ($(target).offset().top)-84.5938
     	},1700);
     	return 0;
    	});
  	});
});

