$(document).ready(() => {
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
		.then(res => res.json())
		.then(data => {
			$("DIV#hello").text(data.hello);
		});
});
