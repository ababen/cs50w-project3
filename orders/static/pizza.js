document.addEventListener('DOMContentLoaded', () => {
    
  // Cache necesarry DOM Elements
  var productsEl = document.querySelector(".products"),
      cartEl =     document.querySelector(".shopping-cart-list"),
      productQuantityEl = document.querySelector(".product-quantity"),
      emptyCartEl = document.querySelector(".empty-cart-btn"),
      cartCheckoutEl = document.querySelector(".cart-checkout"),
      totalPriceEl = document.querySelector(".total-price");


  var getFormContents = function () {

      // Get contents from form
      var form = document.forms[0];
      var name = form.querySelector('input[name="name"]').value;
      var price = form.querySelector('input[name="price"]').value;
      var toppings = form.getElementById('toppings');
      alert(name);

  };
});