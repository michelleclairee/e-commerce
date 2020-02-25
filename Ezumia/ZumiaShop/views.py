from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.http import HttpResponse


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)


# def item_list(request):
#     return HttpResponse("Hello, world. You're at the polls index.")