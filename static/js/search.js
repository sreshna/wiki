var $response = $("#uploadResponse")

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