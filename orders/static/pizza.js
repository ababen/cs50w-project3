document.addEventListener('DOMContentLoaded', () => {
  var ShoppingCart = (function($) {
      "use strict";
      
      // Cache necesarry DOM Elements
      var productsEl = document.querySelector(".products"),
          cartEl =     document.querySelector(".shopping-cart-list"),
          productQuantityEl = document.querySelector(".product-quantity"),
          emptyCartEl = document.querySelector(".empty-cart-btn"),
          cartCheckoutEl = document.querySelector(".cart-checkout"),
          totalPriceEl = document.querySelector(".total-price");
        }


          var getFormContents = function () {
            document.querySelector('submit').onclick {
              // Get contents from form
              var form = document.forms[0];
              var name = form.querySelector('input[name="name"]').value;
              var price = form.querySelector('input[name="price"]').value;
              var toppings = form.getElementById('toppings');
              alert(toppings);


            };
          };

      // Initialize new request
      // const request = new XMLHttpRequest();
      // request.open('POST', '/convert');
      // const data = JSON.parse(request.responseText);
      /* <QueryDict: {'csrfmiddlewaretoken': ['5cZva82xZOb55tuRAtDq9UDZ5Xesb15cncFfOmMIWKCsadPlss4blKGJGDQJNM14'], 
                  'id': ['20'], 
                  'name': ['Steak + Cheese'], 
                  'price': ['6.95'], 
                  'toppings': ['5']
                }> */

      // Fake JSON data array here should be API call
      var products = [
        {
          id: 0,
          name: "iPhone 6S",
          description: "Kogi skateboard tattooed, whatever portland fingerstache coloring book mlkshk leggings flannel dreamcatcher.",
          imageUrl: "http://www.icentar.me/phone/6s/images/goldbig.jpg",
          price: 799
        },
      ],
          productsInCart = [];
      
      // Pretty much self explanatory function. NOTE: Here I have used template strings (ES6 Feature)
      var generateProductList = function() {
        products.forEach(function(item) {
          var productEl = document.createElement("div");
          productEl.className = "product";
          productEl.innerHTML = `<div class="product-image">
                                </div>
                                <div class="product-name"><span>Product:</span> ${item.name}</div>
                                <div class="product-price"><span>Price:</span> ${item.price} $</div>
                                <div class="product-add-to-cart">
                                  <a href="#0" class="button see-more">More Details</a>
                                  <a href="#0" class="button add-to-cart" data-id=${item.id}>Add to Cart</a>
                                </div>
                              </div>
    `;
    // <img src="$item.imageUrl" alt="$item.name">                        
    productsEl.appendChild(productEl);
        });
      }
      
      // Like one before and I have also used ES6 template strings
      var generateCartList = function() {
        
        cartEl.innerHTML = "";
        
        productsInCart.forEach(function(item) {
          var li = document.createElement("li");
          li.innerHTML = `${item.quantity} ${item.product.name} - $${item.product.price * item.quantity}`;
          cartEl.appendChild(li);
        });
        
        productQuantityEl.innerHTML = productsInCart.length;
        
        generateCartButtons()
      }
      
      
      // Function that generates Empty Cart and Checkout buttons based on condition that checks if productsInCart array is empty
      var generateCartButtons = function() {
        if(productsInCart.length > 0) {
          emptyCartEl.style.display = "block";
          cartCheckoutEl.style.display = "block"
          totalPriceEl.innerHTML = "$ " + calculateTotalPrice();
        } else {
          emptyCartEl.style.display = "none";
          cartCheckoutEl.style.display = "none";
        }
      }
      
      // Setting up listeners for click event on all products and Empty Cart button as well
      var setupListeners = function() {
        productsEl.addEventListener("click", function(event) {
          var el = event.target;
          if(el.classList.contains("add-to-cart")) {
          var elId = el.dataset.id;
          addToCart(elId);
          }
        });
        
        emptyCartEl.addEventListener("click", function(event) {
          if(confirm("Are you sure?")) {
            productsInCart = [];
          }
          generateCartList();
        });
      }
      
      // Adds new items or updates existing one in productsInCart array
      var addToCart = function(id) {
        var obj = products[id];
        if(productsInCart.length === 0 || productFound(obj.id) === undefined) {
          productsInCart.push({product: obj, quantity: 1});
        } else {
          productsInCart.forEach(function(item) {
            if(item.product.id === obj.id) {
              item.quantity++;
            }
          });
        }
        generateCartList();
      }
      
      
      // This function checks if project is already in productsInCart array
      var productFound = function(productId) {
        return productsInCart.find(function(item) {
          return item.product.id === productId;
        });
      }
    
      var calculateTotalPrice = function() {
        return productsInCart.reduce(function(total, item) {
          return total + (item.product.price *  item.quantity);
        }, 0);
      }
      
      // This functon starts the whole application
      var init = function() {
        generateProductList();
        setupListeners();
      }
      
      // Exposes just init function to public, everything else is private
      return {
        init: init
      };
      
      // I have included jQuery although I haven't used it
    })(jQuery);
});

ShoppingCart.init();

document.getElementById("form1").onsubmit = getFormContents;