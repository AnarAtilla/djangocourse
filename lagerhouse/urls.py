from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, SupplierViewSet, ProductViewSet, ProductDetailViewSet, AddressViewSet, CustomerViewSet,
    OrderViewSet, OrderItemViewSet, YourModelViewSet, home
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-details', ProductDetailViewSet, basename='product-detail')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-item')
router.register(r'yourmodels', YourModelViewSet, basename='yourmodel')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='lagerhouse-home'),
]