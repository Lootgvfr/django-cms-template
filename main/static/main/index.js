import '../_lib/slick_mod/slick'

$(document).ready(function () {
    $('.quick-gallery').slick({
        arrows: true,
        autoplay: true,
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true,
        focusOnSelect: true
    });
});
