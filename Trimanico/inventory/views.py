from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Inventory


# Create your views here.
def home(request):
    data = {
        "Greetings": "Welcome to TRIMANICO INVENTORY",
        "Facts": "THE BEST INVENTORY IN THE WORLD"
    }
    return JsonResponse(data)

def inventory(request):
    inventories=Inventory.objects.all()
    inventories_data=list(inventories.values())
    return JsonResponse(inventories_data, safe=False)
    
