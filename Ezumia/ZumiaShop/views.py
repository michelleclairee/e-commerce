from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import Item, OrderItem, Order
from .forms import CheckoutForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View


def products(request):
    context = {
        'items': Item.objects.all()
    } 
    return render(request, "product-page.html")

def checkout(request):
    return render(request, "checkout-page.html")
    

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
     
class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
    
    


   