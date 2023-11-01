document.addEventListener("DOMContentLoaded", () => {
  fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
		.then(res => res.json())
		.then(data => {
			$("character").text(data.name);
		});
});
