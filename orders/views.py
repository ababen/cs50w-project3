import json

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from .models import Orders, Pizza, Toppings

def index(request):
    context = {
        "pizza": Pizza.objects.all().filter(category__contains='Pizza'),
        "subs": Pizza.objects.all().filter(category='Subs')
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    # try:
    # username = request.POST["username"]
    # except KeyError:
    #    return render(request, "orders/login.html", {"message": "No username entered."})
    return render(request, "orders/login.html", {"message":None})

def login_action(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
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

def adduser(request):
    # registration = {}
    # registration['email'] = request.POST["email"]
    # registration['password'] = request.POST["password"]
    # registration['lastname'] = request.POST["lastname"]
    # registration['address'] = request.POST["address"]
    # registration['city'] = request.POST["city"]
    # registration['state'] = request.POST["state"]
    # registration['zip'] = request.POST["zip"]
    # registration['phonenumber'] = request.POST["phonenumber"]
    # registration['username'] = request.POST["username"]

    #TypeError possible

    try:
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
    except IntegrityError:
        raise Http404("User already exists.")
    except NameError:
        raise Http404("User already exists.")

    user.last_name = request.POST["lastname"]
    user.first_name = request.POST["firstname"]
    user.save()

    context = {
        "pizza": Pizza.objects.all().filter(category__contains='Pizza'),
        "subs": Pizza.objects.all().filter(category='Subs'),
        "users": User.objects.all(),
        "message": "User created successfully."
    }

    return render(request, "orders/index.html", context)

def addtocart(request, cart):
    # if not request.user.is_authenticated:
    #    return render(request, "orders/login.html", {"message: None"})
    return render(request, "orders/error.html", {"message": cart})

def cart(request):
    #if not request.user.is_authenticated:
    #    return render(request, "orders/login.html", {"message: None"})
    return render(request, "")

def pizza(request, pizza_id):
    #if not request.user.is_authenticated:
    #    return render(request, "orders/login.html", {"message: None"})
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Pizza or food does not exist.")

    toppings = Toppings.objects.all()
    context = {
        "pizza": pizza,
        "toppings": toppings
    }
    return render(request, "orders/pizza.html", context)

def order(request, order_id):
    # if not request.user.is_authenticated:
    #    return render(request, "orders/login.html", {"message: None"})
    try:
        order = Orders.objects.get(pk=order_id)
    except Orders.DoesNotExist:
        raise Http404("Order does not exist.")
    context = {
        "order": order
    }
    return render(request, "orders/order.html", context)
