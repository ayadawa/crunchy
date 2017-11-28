$('ul.ratings li').click(function () {
    var rating = document.querySelector('input[name="rating"]:checked').value;
    console.log(rating);
    $('#id_rating').val(rating);
    $('ul.ratings li').removeClass('active');
    $(this).addClass('active');
    $(this).prevAll().addClass('active');
});

$('ul.ratings li').hover(function () {
    $('ul.ratings li').removeClass('activeHover');
    $(this).addClass('activeHover');
    $(this).prevAll().addClass('activeHover');
}, function () {
    $('ul.ratings li').removeClass('activeHover');
    $(this).prevAll().removeClass('activeHover');
});

window.onload = function() {
    var rating = document.getElementById("id_rating").value;
    var ratingID = "#rat_{rating}".replace(/{rating}/g, rating);
    var selected = $(ratingID);
    selected.addClass('active');
    selected.prevAll().addClass('active');
};