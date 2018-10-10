from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("pizza/<int:pizza_id>", views.pizza, name="pizza"),
    path("<int:order_id>", views.order, name="order")
]

# path("<int:pizza_id>/addtocart", views.addtocart, name="addtocart")
