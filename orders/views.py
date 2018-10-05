from django.http import HttpResponse
from django.shortcuts import render

from .models import Orders

# Create your views here.
def index(request):
    context = {
        "orders": Orders.objects.all()
        # "pizza": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)
