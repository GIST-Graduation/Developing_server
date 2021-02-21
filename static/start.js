$(document).ready(function () {
  setTimeout(function () {
    $(".cover").addClass("fadeOut");
  }, 1500);
  setTimeout(function () {
    $(".cover").addClass("displayNone");
  }, 2500);
  setTimeout(function () {
    $(".ready").removeClass("displayNone").addClass("fadeIn");
  }, 2800);
});
