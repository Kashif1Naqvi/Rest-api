from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    street = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    


class Products(models.Model):
    product_id =  models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=False, auto_now_add=True)
