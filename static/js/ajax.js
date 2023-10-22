/*function toggleFavorite(icon) {
   icon.classList.toggle("fas");
   icon.classList.toggle("far");
   icon.classList.toggle("text-warning");
}*/

function toggleFavorite(icon, product_id) {
    var csrfToken = "{{ csrf_token }}";
    $.ajax({
        type: "GET",
        url: "/add_to_favorite/" + product_id,
        dataType: 'json',
        data: { 'csrfmiddlewaretoken': csrfToken },
        success: function (response) {
            if (response.message == "added") {
                $(icon).toggleClass('text-warning');
            } else {
                $(icon).toggleClass('text-warning');
            }
        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
};


/*var addedToBasket = [];
function toggleBasket(product_id) {
    if (addedToBasket.includes(product_id)) {
        return;
    }

    var csrf_token = "{{ csrf_token }}";
    var button = document.getElementById("basketButton" + product_id);
    var increaseDecreaseDiv = document.getElementById("increase_decrease" + product_id)

    $.ajax({
        type: "GET",
        url: "/add_to_mybasket/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            if (response.message === "success") {
                increaseDecreaseDiv.classList.remove("d-none");
                increaseDecreaseDiv.classList.add("d-flex");
                addedToBasket.push(product_id);
                button.innerText = "Ürün Sepette";
            } else {
                button.innerText = "Sepete Ekle";
            }
        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}*/


var addedToBasket = []; 
function toggleBasket(product_id) {
    if (addedToBasket.includes(product_id)) {
        return;
    }

    var csrf_token = "{{ csrf_token }}";
    var button = document.getElementById("basketButton" + product_id);
    var increaseDecreaseDiv = document.getElementById("increase_decrease" + product_id);

    $.ajax({
        type: "GET",
        url: "/add_to_mybasket/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            message = response.message;
            if (message === "success") {
                increaseDecreaseDiv.classList.remove("d-none");
                increaseDecreaseDiv.classList.add("d-flex");
                addedToBasket.push(product_id);
                button.innerText = "Ürün Sepette";
            } else {
                button.innerText = "Sepete Ekle";
            }
        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}



function toggleIncrease(product_id) {
    var csrf_token = "{{ csrf_token }}";
    var increase_text = document.getElementById("quantityText" + product_id);
    var decrease_button = document.getElementById("decreaseButton" + product_id);
    var total_price_text = document.getElementById("totalPriceText");
    var price_text = document.getElementById("priceText");
    var decreaseBTN = document.getElementById("decreaseBtn" + product_id);

    $.ajax({
        type: "GET",
        url: "/increase/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            increase_text.innerText = response.new_quantity;
            total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
            price_text.innerText = "Toplam Toplam tutar: $" + response.new_total_price;
            if (response.new_quantity > 1) {
                decrease_button.style.display = "inline-block";
                $("#decreaseBtn" + product_id).css("display", "block")
            } else {
                decrease_button.style.display = "none";
                $("#decreaseBtn" + product_id).css("display", "none")
            }

        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}



function toggleDecrease(product_id) {
    var csrf_token = "{{ csrf_token }}"
    var decrease_text = document.getElementById("quantityText" + product_id);
    var decrease_button = document.getElementById("decreaseButton" + product_id);
    var total_price_text = document.getElementById("totalPriceText");
    var price_text = document.getElementById("priceText");
    var decreaseBTN = document.getElementById("decreaseBtn" + product_id);


    $.ajax({
        type: "GET",
        url: "/decrease/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            decrease_text.innerText = response.new_quantity;
            total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
            price_text.innerText = "Toplam Toplam tutar: $" + response.new_total_price;
            if (response.new_quantity == 1) {
                decrease_button.style.display = "none"; 
                $("#decreaseBtn" + product_id).css("display", "none")
            } else {
                decrease_button.style.display = "inline-block";
                $("#decreaseBtn" + product_id).css("display", "block")
            }

        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}



function toggleRemove(product_id) {
    const csrf_token = "{{ csrf_token }}"
    const total_price_text = document.getElementById("totalPriceText");
    const my_product = document.getElementById("myProduct" + product_id);
    const buy_products = document.getElementById("buyProducts");
    const alertElement = document.getElementById("ALERT");
    var price_text = document.getElementById("priceText");

    $.ajax({
        type: "GET",
        url: "/remove/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {

            if (response.new_total_price == "0") {
                total_price_text.style.display = "none";
                buy_products.style.display = "none";
            }

            if (response.message === "deleted") {
                my_product.remove()
                total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
                price_text.innerText = "Toplam Toplam tutar: $" + response.new_total_price;
            }

            if (response.item_quantity === 0) {
                alertElement.style.display = "block";
            }
        },
        error: function () {
            alert("Hata oluştu !")
        },
    });
};



function toggleRemoveFavorite(product_id) {
    var csrf_token = "{{ csrf_token }}"
    var my_favorite = document.getElementById("myFavorite" + product_id);
    const alertElement = document.getElementById("favoriteAlert")

    $.ajax({
        type: "GET",
        url: "/remove_favorite_item/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            console.log(response.message)
            if (response.message == "deleted") {
                my_favorite.remove()
            };

            if (response.item_quantity === 0) {
                alertElement.style.display = "block";
            }
        },
        error: function () {
            alert("Hata oluştu !")
        },
    });
};



function product_remove(product_id) {
    const csrf_token = "{{ csrf_token }}";
    const product = document.getElementById("product" + product_id);
    const product_alert = document.getElementById("product_remove_alert");

    $.ajax({
        type: "GET",
        url: "/product_remove/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            if (response.message == "deleted") {
                product.remove()
            }

            if (response.item_quantity === 0) {
                product_alert.style.display = "block"
            }

        },
        error: function () {
            alert("Hata oluştu !")
        }
    })
}



function change_address() {
    var selectedAddress = $('input[name="selected_address"]:checked').val();
    var csrf_token = "{{ csrf_token }}";

    $.ajax({
        type: 'GET',
        url: 'address',
        data: { 'selected_address': selectedAddress, 'csrfmiddlewaretoken': csrf_token },
        success: function(response) {
            if (response.message === 'success') {
                var newAddress = response.new_address;
                $('#addressElemetId').text("Adres: " + newAddress);
            }
        },
        error: function() {
            alert("Hata oluştu!");
        }
    });
}


function increase(product_title) {
    var encodedTitle = encodeURIComponent(product_title);
    $.ajax({
        type: 'GET',
        url: "/quantity_increase/" + encodedTitle,
        dataType: "json",
        success: function(response) {
            var newQuantity = response.increased_amount;
            $('#quantityContent' + product_title).text(newQuantity);

            if (newQuantity > 1) {
                $("#decreaseBtn" + product_title).css("display", "block");
            }
        },
        error: function() {
            alert("Hata oluştu!");
        }
    });
}



function decrease(product_title) {
    var encodedTitle = product_title;
    $.ajax({
        type: "GET",
        url: "/quantity_decrease/" + encodedTitle,
        dataType: "json",
        success: function(response) {
            var newQuantity = response.decreased_amount;
            $('#quantityContent' + product_title).text(newQuantity);

            if (newQuantity <= 1) {
                $("#decreaseBtn" + product_title).css("display", "none");
            }
        },
        error: function() {
            alert("Hata oluştu!");
        }
    });
}



function errorDecrease(product_id) {
    var decreaseBtn = document.getElementById("decreaseBtn" + product_id)
    $.ajax ({
        type: "GET",
        url: "/decrease/" + product_id,
        dataType: "json",
        success: function(response) {
            if (response.new_quantity <= 1 ){
                decreaseBtn.style.display = "none"
            }
        },
        error: function() {
            alert("Hata oluştu!")
        }
    })
}


function errorIncrease(product_id) {
    var decreaseBtn = document.getElementById("decreaseBtn" + product_id)
    $.ajax ({
        type: "GET",
        url: "/increase/" + product_id,
        dataType: "json",
        success: function(response) {
            if (response.new_quantity > 1 ){
                decreaseBtn.style.display = "inline-block"
            }
        },
        error: function() {
            alert("Hata oluştu!");
        }
    })
}