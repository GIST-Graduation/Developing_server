$(document).ready(function () {
  $("#content1_title").click(function () {
    $(".content").removeClass("hide");
    $(".content").addClass("hide");
    $("#content1").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content1_title").addClass("active");
  });

  $("#content2_title").click(function () {
    $(".content").removeClass("hide");
    $(".content").addClass("hide");
    $("#content2").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content2_title").addClass("active");
  });

  $("#content3_title").click(function () {
    $(".content").removeClass("hide");
    $(".content").addClass("hide");
    $("#content3").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content3_title").addClass("active");
  });

  $("#content4_title").click(function () {
    $(".content").removeClass("hide");
    $(".content").addClass("hide");
    $("#start").removeClass("hide");

    $(".content_nav").removeClass("active");
    $("#content4_title").addClass("active");
  });
});