# lagerhouse/urls.py
from django.urls import path
from .views import (
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
    SupplierListCreateView, SupplierRetrieveUpdateDestroyView,
    ProductListCreateView, ProductRetrieveUpdateDestroyView,
    ProductDetailListCreateView, ProductDetailRetrieveUpdateDestroyView,
    AddressListCreateView, AddressRetrieveUpdateDestroyView,
    CustomerListCreateView, CustomerRetrieveUpdateDestroyView,
    OrderListCreateView, OrderRetrieveUpdateDestroyView,
    OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView,
    YourModelListCreateView, YourModelRetrieveUpdateDestroyView,
    home
)

urlpatterns = [
    path('', home, name='home'),  # Добавьте этот путь для корневого URL
    path('home/', home, name='home'),  # Этот путь также остается для совместимости
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('product-details/', ProductDetailListCreateView.as_view(), name='productdetail-list-create'),
    path('product-details/<int:pk>/', ProductDetailRetrieveUpdateDestroyView.as_view(), name='productdetail-detail'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDestroyView.as_view(), name='address-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyView.as_view(), name='orderitem-detail'),
    path('yourmodels/', YourModelListCreateView.as_view(), name='yourmodel-list-create'),
    path('yourmodels/<int:pk>/', YourModelRetrieveUpdateDestroyView.as_view(), name='yourmodel-detail'),
]