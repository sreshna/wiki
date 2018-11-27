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
    url: '/suggest/',
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
    console.log(title)
    $.ajax({
    type: "get",
    dataType: 'json',
    contentType: 'json',
    crossDomain: true,
    url: '/favorite/',
    data: {"title": title},
    success: function(context) {
    console.log(context);
    $favorite_response.empty();
    $favorite_response.append(context);
      }
    })
});