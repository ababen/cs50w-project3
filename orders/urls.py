from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("login_action", views.login_action, name="login_action"),
    path("logout", views.logout_view, name="logout"),
    path("adduser", views.adduser, name="adduser"),
    path("addtocart", views.addtocart, name="addtocart"),
    path("register", views.register, name="register"),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    path("pizza/<int:pizza_id>", views.pizza, name="pizza"),
    path("<int:order_id>", views.order, name="order")
]

# path("<int:pizza_id>/addtocart", views.addtocart, name="addtocart")
