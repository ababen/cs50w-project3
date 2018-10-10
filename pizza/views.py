from django.http import HttpResponse, Http404
from django.shortcuts import render

from orders.models import Pizza

# Create your views here.
def index(request):
    context = {
        "pizza": Pizza.objects.all()
    }
    return render(request, "pizza/index.html", context)

# Need to redict to home page
