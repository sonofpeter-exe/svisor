$(function() {
    $(".slider").owlCarousel({
        loop: false,
        center: false,
        items: 3,
        // margin: 10,
        autoWidth: true,
        autoplay: false,
        autoplayTimeout: 5000,
        autoplayHoverPause: false,
        responsive: {
            0: {
                dotsEach: 3,
                items: 5,
                nav: false
            },
            500: {
                dotsEach: false
            }
        }
    })
});

// toggle filter
$(function() { 
    $("#pagi-filter").click(function() {
        $("#tmp-filter").toggle({"display": "block"});
        $("#overlay").toggle();
        $("body").css({"position": "fixed", "width": "100%"});
    });
});

$(function() { 
    $("#overlay").click(function() {
        $("#tmp-filter").toggle({"display": "none"});
        $("#tmp-list").toggle({"display": "none"});
        $("#overlay").css({"display": "none"});
        $("body").css({"position": "relative"});
    });
});


