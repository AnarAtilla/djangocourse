# lagerhouse/views.py
from rest_framework import generics
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem, YourModel
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer, ProductDetailSerializer, AddressSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, YourModelSerializer
from .filters import CategoryFilter, SupplierFilter, ProductFilter, ProductDetailFilter, AddressFilter, CustomerFilter, OrderFilter, OrderItemFilter, YourModelFilter
from django.shortcuts import render

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer
    filterset_class = SupplierFilter

class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductDetailListCreateView(generics.ListCreateAPIView):
    queryset = ProductDetail.objects.all().order_by('id')
    serializer_class = ProductDetailSerializer
    filterset_class = ProductDetailFilter

class ProductDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all().order_by('id')
    serializer_class = ProductDetailSerializer

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
    filterset_class = AddressFilter

class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter

class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all().select_related('product', 'order').order_by('id')
    serializer_class = OrderItemSerializer

class YourModelListCreateView(generics.ListCreateAPIView):
    queryset = YourModel.objects.all().order_by('id')
    serializer_class = YourModelSerializer
    filterset_class = YourModelFilter

class YourModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YourModel.objects.all().order_by('id')
    serializer_class = YourModelSerializer

def home(request):
    return render(request, 'lagerhouse/home.html')