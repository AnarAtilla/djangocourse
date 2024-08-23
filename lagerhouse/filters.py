# lagerhouse/filters.py
import django_filters
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem, YourModel

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']

class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'phone_number']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'category', 'supplier', 'price', 'quantity', 'article', 'available']

class ProductDetailFilter(django_filters.FilterSet):
    class Meta:
        model = ProductDetail
        fields = ['product', 'description', 'manufacturing_date', 'expiration_date', 'weight']

class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = ['country', 'city', 'street', 'house']

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_joined', 'deleted', 'deleted_at']

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['order_date', 'customer']

class OrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']

class YourModelFilter(django_filters.FilterSet):
    class Meta:
        model = YourModel
        fields = ['name', 'description', 'created_at']