$(document).ready(() => {
  $("DIV#add_item").click(() =>  {
    $("<li>").text("Item").appendTo("ul.my_list");
  });
});
