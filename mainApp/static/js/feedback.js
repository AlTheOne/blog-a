$(document).ready(function(){
	$('#send-button').on('click', function(e){
		e.preventDefault();
		$.ajax({
			url: 'https://kadyrova-aygul.ru/feedback/',
			method: 'POST',
			data: $("#feedback_form").serialize(),
			cached: true,
			success: function(info){
				console.log(info);
				if(info.data['status'] == 'Invalid reCAPTCHA. Please try again.'){
					$('.feedback-info').text('Неверная капча.');
				}
				if(info.data['status'] == 'Error: Invalid form'){
					$('.feedback-info').text('Неверно заполнена форма.');
				}
				if(info.data['status'] == 'OK'){
					location.reload();
				}
			},
			error: function(e){
				console.log(e);
			}
		})
	})
})