document.readyState(() => {
  $("DIV#red_header").click(() => {
    $("header").addClass("red");
  });
});
