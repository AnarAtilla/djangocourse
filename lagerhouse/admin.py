from django.contrib import admin

from .models import Category, Supplier, Product, ProductDetail, Address, Order, OrderItem, Customer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email', 'phone_number')
    ordering = ('name',)


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    can_delete = False
    verbose_name_plural = 'Product Details'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price', 'quantity', 'article', 'available')
    list_filter = ('category', 'supplier', 'available')
    search_fields = ('name', 'article')
    ordering = ('category', 'quantity')
    list_editable = ('price', 'quantity', 'available')
    inlines = [ProductDetailInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house')
    search_fields = ('country', 'city', 'street', 'house')
    ordering = ('country', 'city', 'street')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'customer')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__email')
    ordering = ('-order_date',)
    inlines = [OrderItemInline]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'deleted')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('-date_joined',)
