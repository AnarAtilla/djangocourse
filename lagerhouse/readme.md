# Lagerhaus APP

## Описание

Lagerhaus - это приложение для управления складом, которое позволяет управлять продуктами, категориями, поставщиками,
заказами и клиентами.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd lagerhaus
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

## Использование

После запуска сервера, вы можете получить доступ к приложению по
адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Вот основные URL-адреса:

- `/admin/`: Административная панель Django.
- `/products/`: Список продуктов.
- `/orders/`: Список заказов.
- `/customers/`: Список клиентов.

## Модели

### Category

- `name`: CharField (max_length=40, unique=True)

### Supplier

- `name`: CharField (max_length=100, unique=True)
- `contact_email`: EmailField (unique=True)
- `phone_number`: CharField (max_length=20, unique=True)

### Product

- `name`: CharField (max_length=100)
- `category`: ForeignKey (Category, on_delete=models.PROTECT, related_name='products')
- `supplier`: ForeignKey (Supplier, on_delete=models.PROTECT, related_name='products')
- `price`: DecimalField (max_digits=10, decimal_places=2)
- `quantity`: PositiveSmallIntegerField
- `article`: CharField (max_length=100, unique=True, help_text='Unique string product id', db_index=True)
- `available`: BooleanField (default=True)

### ProductDetail

- `product`: OneToOneField (Product, on_delete=models.CASCADE, related_name='details')
- `description`: TextField (null=True, blank=True)
- `manufacturing_date`: DateField (null=True, blank=True)
- `expiration_date`: DateField (null=True, blank=True)
- `weight`: DecimalField (null=True, blank=True, max_digits=5, decimal_places=2)

### Address

- `country`: CharField (max_length=100)
- `city`: CharField (max_length=100)
- `street`: CharField (max_length=255)
- `house`: CharField (max_length=6)

### Customer

- `first_name`: CharField (max_length=50)
- `last_name`: CharField (max_length=50)
- `email`: EmailField (unique=True)
- `phone_number`: CharField (max_length=15)
- `address`: OneToOneField (Address, null=True, on_delete=models.SET_NULL, related_name='customer')
- `date_joined`: DateTimeField (auto_now_add=True)
- `deleted`: BooleanField (default=False)
- `deleted_at`: DateTimeField (null=True, blank=True)

### Order

- `order_date`: DateTimeField (auto_now_add=True)
- `customer`: ForeignKey (Customer, on_delete=models.PROTECT, related_name='orders')

### OrderItem

- `order`: ForeignKey (Order, on_delete=models.CASCADE, related_name='order_items')
- `product`: ForeignKey (Product, on_delete=models.PROTECT, related_name='order_items')
- `quantity`: PositiveSmallIntegerField
- `price`: DecimalField (max_digits=10, decimal_places=2)

## Административная панель

Для управления моделями через административную панель Django, зарегистрируйте модели в `admin.py`:

```python
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
```

## Лицензия

Этот проект лицензирован под лицензией MIT.

## Контактные данные

Этот `README.md` файл предоставляет основную информацию о проекте, его установке и использовании, а также контактные
данные автора. Это поможет другим студентам и преподавателям быстро понять суть проекта и его возможности.