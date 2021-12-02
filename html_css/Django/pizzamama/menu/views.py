from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizzas.nom + " : " + str(pizzas.prix) + "€ "  for pizzas in pizzas]
    pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)   
    return HttpResponse("Les pizzas : " + pizzas_names_and_price_str)
