setInterval(function() {
    if sessionStorage['id'] {
        statusCheck(myDomain, sessionStorage['id']);
    }
}, 1000);


// buttonAddToCart event handler
$(document).ready(
    buttonAddToCart.onclick = function() {
        add_to_cart();
    }

    function add_to_cart() {
        $.ajax({
            url: '../cart/add/',
            data: {bookInstId:$('#bookInstId').text()},

            success: function() {
                $('#modalAddToCart').modal('show')
            }
        });
    }

    $('.btn-add-to-cart').click(function() {
        alert($(this).prev().find('span#bookInstId').text());
        // add_to_cart();
    });

    function add_to_cart() {
        $.ajax({
            url: "{% url 'add-to-cart' %}",
            data: {
                pk:$(this).closest('#bookInstId').innerHTML()
                // title:$('#book-title').text()
            },

            success: function() {
                $('#modalAddToCart').modal('show')
            }
        });
    }
);
