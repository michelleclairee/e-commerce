from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    products,
    HomeView
)
app_name = 'ZumiaShop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<pk>/', ItemDetailView.as_view(), name='product')
]