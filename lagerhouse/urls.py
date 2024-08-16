# lagerhouse/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('suppliers/', views.SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('product-details/', views.ProductDetailListCreateView.as_view(), name='productdetail-list-create'),
    path('product-details/<int:pk>/', views.ProductDetailRetrieveUpdateDestroyView.as_view(), name='productdetail-detail'),
    path('addresses/', views.AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', views.AddressRetrieveUpdateDestroyView.as_view(), name='address-detail'),
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('order-items/', views.OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', views.OrderItemRetrieveUpdateDestroyView.as_view(), name='orderitem-detail'),
    path('yourmodel/', views.YourModelListCreateView.as_view(), name='yourmodel-list-create'),
    path('yourmodel/<int:pk>/', views.YourModelRetrieveUpdateDestroyView.as_view(), name='yourmodel-detail'),
    path('home/', views.home, name='home'),
]




# Перейдите по ссылкам на ваши API Например:
#
# Home Page: http://127.0.0.1:8000/lagerhouse/home/
#
# Categories: http://127.0.0.1:8000/lagerhouse/categories/
#
# Suppliers: http://127.0.0.1:8000/lagerhouse/suppliers/
#
# Products: http://127.0.0.1:8000/lagerhouse/products/
#
# Product Details: http://127.0.0.1:8000/lagerhouse/product-details/
#
# Addresses: http://127.0.0.1:8000/lagerhouse/addresses/
#
# Customers: http://127.0.0.1:8000/lagerhouse/customers/
#
# Orders: http://127.0.0.1:8000/lagerhouse/orders/
#
# Order Items: http://127.0.0.1:8000/lagerhouse/order-items/
#
# Your Model: http://127.0.0.1:8000/lagerhouse/yourmodel/