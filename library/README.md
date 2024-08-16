# Library Project

## Описание

Library - это приложение для управления библиотекой, которое позволяет управлять книгами, авторами, издателями, читателями и заказами. Приложение также предоставляет REST API с использованием Django REST Framework (DRF).

## REST API

Приложение предоставляет следующие эндпойнты:

- `/api/books/`: Список книг (GET, POST).
- `/api/books/<id>/`: Детали книги (GET, PUT, PATCH, DELETE).
- `/api/authors/`: Список авторов (GET, POST).
- `/api/authors/<id>/`: Детали автора (GET, PUT, PATCH, DELETE).
- `/api/publishers/`: Список издателей (GET, POST).
- `/api/publishers/<id>/`: Детали издателя (GET, PUT, PATCH, DELETE).
- `/api/readers/`: Список читателей (GET, POST).
- `/api/readers/<id>/`: Детали читателя (GET, PUT, PATCH, DELETE).
- `/api/orders/`: Список заказов (GET, POST).
- `/api/orders/<id>/`: Детали заказа (GET, PUT, PATCH, DELETE).

## Модели

### Author
- `first_name`: CharField (max_length=50)
- `last_name`: CharField (max_length=50)
- `birth_date`: DateField (null=True, blank=True)

### Publisher
- `name`: CharField (max_length=100, unique=True)
- `address`: CharField (max_length=255, null=True, blank=True)
- `website`: URLField (null=True, blank=True)

### Book
- `title`: CharField (max_length=200)
- `author`: ForeignKey (Author, on_delete=models.PROTECT, related_name='books')
- `publisher`: ForeignKey (Publisher, on_delete=models.PROTECT, related_name='books')
- `publication_date`: DateField (null=True, blank=True)
- `isbn`: CharField (max_length=13, unique=True)
- `price`: DecimalField (max_digits=10, decimal_places=2)
- `stock`: IntegerField

### Reader
- `first_name`: CharField (max_length=50)
- `last_name`: CharField (max_length=50)
- `email`: EmailField (unique=True)
- `phone_number`: CharField (max_length=15)
- `address`: CharField (max_length=255, null=True, blank=True)
- `date_joined`: DateTimeField (auto_now_add=True)

### Order
- `order_date`: DateTimeField (auto_now_add=True)
- `reader`: ForeignKey (Reader, on_delete=models.PROTECT, related_name='orders')

### OrderItem
- `order`: ForeignKey (Order, on_delete=models.CASCADE, related_name='order_items')
- `book`: ForeignKey (Book, on_delete=models.PROTECT, related_name='order_items')
- `quantity`: PositiveSmallIntegerField
- `price`: DecimalField (max_digits=10, decimal_places=2)

## Административная панель

Для управления моделями через административную панель Django, зарегистрируйте модели в `admin.py`:

```python
from django.contrib import admin
from .models import Author, Publisher, Book, Reader, Order, OrderItem

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'isbn', 'price', 'stock')
    list_filter = ('author', 'publisher')
    search_fields = ('title', 'isbn')
    ordering = ('title',)

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('-date_joined',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'reader')
    search_fields = ('reader__first_name', 'reader__last_name', 'reader__email')
    ordering = ('-order_date',)
    inlines = [OrderItemInline]