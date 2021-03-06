$(document).ready(function () {
  $("#content1_title").click(function () {
    $(".introduction").removeClass("hide");
    $(".introduction").addClass("hide");
    $("#Fe").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content1_title").addClass("active");
  });

  $("#content2_title").click(function () {
    $(".introduction").removeClass("hide");
    $(".introduction").addClass("hide");
    $("#rejaealsun").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content2_title").addClass("active");
  });

  $("#content3_title").click(function () {
    $(".introduction").removeClass("hide");
    $(".introduction").addClass("hide");
    $("#silver_plate").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content3_title").addClass("active");
  });

  $("#content4_title").click(function () {
    $(".introduction").removeClass("hide");
    $(".introduction").addClass("hide");
    $("#strix").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content4_title").addClass("active");
  });
});