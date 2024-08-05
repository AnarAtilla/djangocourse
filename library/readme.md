# Library Project

## Описание
Library - это приложение для управления библиотекой, которое позволяет управлять книгами, авторами, издателями, читателями и заказами.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd library
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

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
```

## Лицензия

Этот проект лицензирован под лицензией MIT.