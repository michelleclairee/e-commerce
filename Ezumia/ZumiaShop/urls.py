from django.urls import path
from .views import (
    home,
    checkout,
    products,
    HomeView
)
app_name = 'ZumiaShop'

urlpatterns = [
    path('', HomeView.as_view, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products')
]