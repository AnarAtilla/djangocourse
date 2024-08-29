from rest_framework import viewsets
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem, YourModel
from .serializers import (
    LagerhouseCategorySerializer, LagerhouseSupplierSerializer, LagerhouseProductSerializer, LagerhouseProductDetailSerializer,
    LagerhouseAddressSerializer, LagerhouseCustomerSerializer, LagerhouseOrderSerializer, LagerhouseOrderItemSerializer,
    LagerhouseYourModelSerializer
)
from .filters import (
    CategoryFilter, SupplierFilter, ProductFilter, ProductDetailFilter, AddressFilter, CustomerFilter, OrderFilter,
    OrderItemFilter, YourModelFilter
)
from django.shortcuts import render

class BaseViewSet(viewsets.ModelViewSet):
    filterset_fields = '__all__'

class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = LagerhouseCategorySerializer
    filterset_class = CategoryFilter

class SupplierViewSet(BaseViewSet):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = LagerhouseSupplierSerializer
    filterset_class = SupplierFilter

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = LagerhouseProductSerializer
    filterset_class = ProductFilter

class ProductDetailViewSet(BaseViewSet):
    queryset = ProductDetail.objects.all().order_by('id')
    serializer_class = LagerhouseProductDetailSerializer
    filterset_class = ProductDetailFilter

class AddressViewSet(BaseViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = LagerhouseAddressSerializer
    filterset_class = AddressFilter

class CustomerViewSet(BaseViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = LagerhouseCustomerSerializer
    filterset_class = CustomerFilter

class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = LagerhouseOrderSerializer
    filterset_class = OrderFilter

class OrderItemViewSet(BaseViewSet):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = LagerhouseOrderItemSerializer
    filterset_class = OrderItemFilter

class YourModelViewSet(BaseViewSet):
    queryset = YourModel.objects.all().order_by('id')
    serializer_class = LagerhouseYourModelSerializer
    filterset_class = YourModelFilter

def home(request):
    return render(request, 'lagerhouse/home.html')