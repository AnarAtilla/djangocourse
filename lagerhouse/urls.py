from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, SupplierViewSet, ProductViewSet, ProductDetailViewSet, AddressViewSet, CustomerViewSet,
    OrderViewSet, OrderItemViewSet, YourModelViewSet, UserOwnedObjectsView, home, StatisticsView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-details', ProductDetailViewSet, basename='product-detail')
router.register(r'addresses', AddressViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet, basename='order-item')
router.register(r'yourmodels', YourModelViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Your API description",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('my-objects/', UserOwnedObjectsView.as_view(), name='my-objects'),
    path('home/', home, name='lagerhouse-home'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]