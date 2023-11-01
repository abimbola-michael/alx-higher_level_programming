document.readyState(() => {
  $("DIV#red_header").click(() => {
    $("header").toggleClass("red green");
  });
});
