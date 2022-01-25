const contract = function() {
  if ($("input").is(":checked")) {
    $(".product-info").css({"opacity":"1.0", "display": "inline-block"})
    $(".product").width("15%")
    $(".product").height("15%")
    $(".product-info").height("95%")
    $(".product-info").width("73%")
  } else {
    $(".product").width("100%")
    $(".product").height("98%")
    $(".product-info").height("0px")
    $(".product-info").width("0px")
    $(".product-info").css({"opacity":"0"})
  };
 }

const drop = function(obj) {
  let node = $(obj).attr('id')
  $("#" + node + "-ops").slideToggle(200);
}

// input suggestion

$(function(){
    $("input[type='search']").keyup(function(){
        $('span').text(function(i, oldText) {
    return oldText.toLowerCase();
  })

  let buff = "span:not(:contains(" + $('#' + $(this).attr("id")).val() +  "))"; 
  let rbuff = "span:contains(" + $('#' + $(this).attr("id")).val() +  ")";
   
   
  if ($(rbuff)) {
    $(rbuff).css({"display" : "inline-block"})
    $(buff).css({"display": "none"})
  } 
   
  $.each($(rbuff), function(index, value){
    console.log(index + ": " + value.innerHTML );
  });
    })
})

// toggle select class
$(function(){
    $("span").click(function(){
      if ($(this).attr("class") == "selected") {
        $(this).removeClass("selected")
       } else {
         $(this).addClass("selected")
       }
    })
})
