var $response = $("#uploadResponse");
var $favorite_response = $("#favoriteResponse");

$("#search_button").click(function(e) {
    e.preventDefault();
    var q = $("#search_parameter").val();
      $.ajax({
    type: "GET",
    url: '/search/',
    data: {"q": q},
    success: function(response) {
    $response.empty();
    $response.append(response);
      }
    })
});

$('.suggestSubmit').click(function(e) {
    e.preventDefault();
    var q = $(this).val();
    $.ajax({
    type: "GET",
    url: '/search/',
    data: {"q": q},
    success: function(response) {
    $response.empty();
    $response.append(response);
      }
    })
});

$('#add_to_favorite').click(function(e) {
    e.preventDefault();
    var title = $("#favoriteTitle").val();
    $.ajax({
    type: "get",
    dataType: 'json',
    contentType: 'json',
    crossDomain: true,
    url: '/favorite/',
    data: {"title": title},
    success: function(context) {
    $favorite_response.empty();
    $favorite_response.append(context);
      }
    })
});


$('.lang_option').on('change',function() {
    e.preventDefault();
    console.log(e);
    console.log($(this));
    var q = $(this).val();
    $.ajax({
    type: "GET",
    url: '/language/',
    data: {"q": q},
    success: function(response) {
    $response.empty();
    $response.append(response);
      }
    })
});

$('.favoriteSubmit').click(function(e) {
    e.preventDefault();
    var q = $(this).val();
    $.ajax({
    type: "GET",
    url: '/favorites/',
    data: {"q": q},
    success: function(response) {
    $favorite_response.empty();
    $favorite_response.append(response);
      }
    })
});