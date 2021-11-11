$(document).ready(function() {
	var $myForm = $('.my-form')
	var $mybtn = $('.btn')

	$myForm.submit(function (event) {
		event.preventDefault()
		var $thisURL = $myForm.attr('data-url') || window.location.href 
		var $formData = $(this).serialize()
		$.ajax({
			method: "POST",
			url: $thisURL,
			data: $formData,
			success: handleFormSuccess,
			error: handleFormError,
		})
	})
	$mybtn.click(function () {

		$.ajax({
			method: "POST",
			url: 'logout',
			success: handleLogoutSuccess,
			error: handleLogoutError,
		})
	})

	function handleFormSuccess(data, textStatus, jqXHR) {
		console.log(data)
		console.log(textStatus)
		console.log(jqXHR)
		$('#body').html(data)
	}

	function handleFormError(jqXHR, textStatus, errorThrown) {
		console.log(jqXHR)
		console.log(textStatus)
		console.log(errorThrown)
	}

	function handleLogoutSuccess(data) {
		console.log("logout success")
		$('#body').html(data)
	}

	function handleLogoutError() {
	}
});