from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from .models import Orders, Pizza

# Create your views here.
def index(request):
#   Use this code to make sure someone is logged in
#    if not request.user.is_authenticated:
#        return render(request, "orders/login.html", {"message: None"})
    context = {
        "pizza": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)


def login_view(request):
    try:
        username = request.POST["username"]
    except KeyError:
        return render(request, "orders/login.html", {"message": "No username entered."})

    password = request.POST["password"]
    user = authenticated(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message":"Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Loged out."})


def register(request):
    return render(request, "orders/register.html")

def register2(request):
    try:
        firstname = str(request.POST["firstname"])
    except KeyError:
        return render(request, "orders/error.html", {"message": "No input"})

# How to redirect users
# return HttpResponseRedirect(reverse("flight", args=(flight_id)))

# def addtocart(request):
    # return render(request, "")

def pizza(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Pizza or food does not exist.")
    context = {
        "pizza": pizza
    }
    return render(request, "pizza/pizza.html", context)

def order(request, order_id):
    try:
        order = Orders.objects.get(pk=order_id)
    except Orders.DoesNotExist:
        raise Http404("Order does not exist.")
    context = {
        "order": order
    }
    return render(request, "orders/order.html", context)
