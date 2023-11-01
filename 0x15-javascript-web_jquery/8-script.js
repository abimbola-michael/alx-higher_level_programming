document.addEventListener("DOMContentLoaded", () => {
  fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
		.then(res => res.json())
		.then(data => {
			data.results.forEach((film) => {
				$("<li>").text(film.title).appendTo("ul#list_movies");
			})
		});
});
