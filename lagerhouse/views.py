from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import (
    CategoryFilter, SupplierFilter, ProductFilter, ProductDetailFilter, AddressFilter, CustomerFilter, OrderFilter,
    OrderItemFilter, YourModelFilter
)
from .models import Category, Supplier, ProductDetail, Address, OrderItem, YourModel
from .models import Order, Customer, Product
from .permissions import CanViewStatistics
from .permissions import IsCustomerOrReadOnly
from .serializers import (
    LagerhouseCategorySerializer, LagerhouseSupplierSerializer, LagerhouseProductSerializer,
    LagerhouseProductDetailSerializer,
    LagerhouseAddressSerializer, LagerhouseCustomerSerializer, LagerhouseOrderItemSerializer,
    LagerhouseYourModelSerializer
)
from .serializers import LagerhouseOrderSerializer


class BaseViewSet(viewsets.ModelViewSet):
    filterset_fields = '__all__'
    permission_classes = [IsCustomerOrReadOnly]


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


class UserOwnedObjectsView(APIView):
    permission_classes = [IsCustomerOrReadOnly]

    def get(self, request, format=None):
        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)

        owned_orders = Order.objects.filter(customer=user.customer)
        serializer = LagerhouseOrderSerializer(owned_orders, many=True)
        return Response(serializer.data)


class StatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated, CanViewStatistics]

    def get(self, request, format=None):
        # Здесь вы можете добавить логику для сбора статистики
        total_orders = Order.objects.count()
        total_customers = Customer.objects.count()
        total_products = Product.objects.count()

        statistics = {
            'total_orders': total_orders,
            'total_customers': total_customers,
            'total_products': total_products,
        }
        return Response(statistics)


def home(request):
    return render(request, 'lagerhouse/home.html')
