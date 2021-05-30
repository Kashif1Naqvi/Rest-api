from django.db.models.query_utils import RegisterLookupMixin
from django.http.response import HttpResponse
from rest_framework.response import Response
from .models import Customer, Products, Order
from rest_framework.parsers import JSONParser
from .serializers import CustomerSerializer, ProductSerializer , OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customer_list(request):
    
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    """
    Retrieve, update or delete a customer_detail.
    """
    try:
        customers = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status= status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a product_detail.
    """
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def order_api():
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)