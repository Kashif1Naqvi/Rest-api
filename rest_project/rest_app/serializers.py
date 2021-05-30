from django.db.models import fields
from rest_framework import serializers
from .models import Customer, Order, Products

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user_id','customer_id','first_name','last_name','phone','email','street','city','state','zip_code']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields= ['product_id','product_name','product_description']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= '__all__'


