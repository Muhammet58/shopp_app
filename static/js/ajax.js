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
            $(icon).toggleClass('text-warning');
        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
};


var addedToBasket = [];
function toggleBasket(product_id) {
    if (addedToBasket.includes(product_id)) {
        return;
    }

    var csrf_token = "{{ csrf_token }}";
    var button = document.getElementById("basketButton" + product_id);
    var buttonModal = document.getElementById("basketButtonModal" + product_id);

    $.ajax({
        type: "GET",
        url: "/add_to_mybasket/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            addedToBasket.push(product_id);
            button.innerText = "Ürün Sepette";
            buttonModal.innerText = "Ürün Sepette";

        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}




function toggleIncrease(product_id) {
    var csrf_token = "{{ csrf_token }}";
    var increase_text = document.getElementById("quantityText" + product_id);
    var increase_button = document.getElementById("increaseButton" + product_id);
    var decrease_button = document.getElementById("decreaseButton" + product_id);
    var total_price_text = document.getElementById("totalPriceText");

    $.ajax({
        type: "GET",
        url: "/increase/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            increase_text.innerText = response.new_quantity;
            total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
            if (response.new_quantity > 1) {
                decrease_button.style.display = "inline-block";
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

    $.ajax({
        type: "GET",
        url: "/decrease/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            decrease_text.innerText = response.new_quantity;
            total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
            if (response.new_quantity == 1) {
                decrease_button.style.display = "none";
            }

        },
        error: function () {
            alert("Hata oluştu !");
        },
    });
}


function toggleRemove(product_id) {
    var csrf_token = "{{ csrf_token }}"
    var total_price_text = document.getElementById("totalPriceText");
    var my_product = document.getElementById("myProduct" + product_id);
    var buy_products = document.getElementById("buyProducts");

    $.ajax({
        type: "GET",
        url: "/remove/" + product_id,
        dataType: "json",
        data: { "csrfmiddlewaretoken": csrf_token },
        success: function (response) {
            if (response.message === "deleted") {
                my_product.remove()
                total_price_text.innerText = "Toplam ücret: $" + response.new_total_price;
            }

            if (response.new_total_price == "0") {
                total_price_text.style.display = "none";
                buy_products.style.display = "none";
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
        },
        error: function () {
            alert("Hata oluştu !")
        },
    });
};


