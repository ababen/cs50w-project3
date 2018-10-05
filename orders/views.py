from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Orders, Pizza

# Create your views here.
def index(request):
    context = {
        "orders": Orders.objects.all()
    }
    return render(request, "orders/index.html", context)

def order(request, order_id):
    try:
        order = Orders.objects.get(pk=order_id)
    except Orders.DoesNotExist:
        raise Http404("Order does not exist.")
    context = {
        "order": order
    }
    return render(request, "orders/order.html", context)
