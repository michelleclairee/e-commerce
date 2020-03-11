from django.conf import settings
from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sports wear'),
    ('OW', 'Outwear'),
)
 
LABEL_CHOICES = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'Danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    
    def __str__(self):
        return self.title

  

class OrderItem(models.Model):  # items in the cart
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):  # class for the users orders
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        auto_now_add=True)  # moment the order was created
    ordered_date = models.DateTimeField()
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username