from django.http import HttpResponse, Http404
from django.shortcuts import render

from orders.models import Pizza, Toppings

# Create your views here.
def index(request):
    context = {
        "pizza": Pizza.objects.all()
    }
    return render(request, "pizza/index.html", context)

def pizza(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Pizza does not exist.")
    context = {
        "pizza": pizza,
        "toppings": Toppings.objects.all()
    }
    return render(request, "pizza/pizza.html", context)
