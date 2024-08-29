from rest_framework import serializers
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem, YourModel

class LagerhouseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class LagerhouseSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_email', 'phone_number']

class LagerhouseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'supplier', 'price', 'quantity', 'article', 'available']

class LagerhouseProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'product', 'description', 'manufacturing_date', 'expiration_date', 'weight']

class LagerhouseAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'street', 'house']

class LagerhouseCustomerSerializer(serializers.ModelSerializer):
    address = LagerhouseAddressSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_joined', 'deleted', 'deleted_at']

class LagerhouseOrderSerializer(serializers.ModelSerializer):
    customer = LagerhouseCustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'customer']

class LagerhouseOrderItemSerializer(serializers.ModelSerializer):
    product = LagerhouseProductSerializer()
    order = LagerhouseOrderSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

class LagerhouseYourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = ['id', 'name', 'description', 'created_at']