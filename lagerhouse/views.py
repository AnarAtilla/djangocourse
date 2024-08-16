# lagerhouse/views.py
from rest_framework import generics
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem, YourModel
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer, ProductDetailSerializer, AddressSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, YourModelSerializer
from django.shortcuts import render

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailListCreateView(generics.ListCreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

class ProductDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class YourModelListCreateView(generics.ListCreateAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

class YourModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

def home(request):
    return render(request, 'lagerhouse/home.html')