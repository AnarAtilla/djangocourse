from lagerhouse.models import Customer, Product, Order, OrderItem
from django.utils import timezone
from random import choice, randint
from datetime import timedelta
from django.db import IntegrityError, transaction

# Функция для генерации случайной даты в пределах последних двух лет
def random_date_within_last_2_years():
    end_date = timezone.now()
    start_date = end_date - timedelta(days=730)  # 2 года
    return start_date + timedelta(seconds=randint(0, int((end_date - start_date).total_seconds())))

# Получение всех клиентов и продуктов
customers = list(Customer.objects.all())
products = list(Product.objects.all())

# Проверка, что список клиентов не пуст
if not customers:
    raise ValueError("Список клиентов пуст. Убедитесь, что в базе данных есть клиенты.")

# Создание 100 заказов
for _ in range(100):
    # Выбор случайного клиента
    customer = choice(customers)

    # Проверка, что клиент существует
    if customer:
        try:
            with transaction.atomic():
                # Создание заказа с случайной датой
                order = Order.objects.create(
                    customer=customer,
                    order_date=random_date_within_last_2_years()
                )

                # Случайное количество позиций в заказе от 1 до 5
                num_items = randint(1, 5)
                for _ in range(num_items):
                    # Выбор случайного продукта
                    product = choice(products)

                    # Случайное количество от 1 до 5
                    quantity = randint(1, 5)

                    # Цена за единицу продукта
                    price = product.price

                    # Создание позиции заказа
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=price
                    )

                    # Обновление количества продукта на складе
                    product.quantity -= quantity
                    product.save()
        except IntegrityError as e:
            print(f"Ошибка при создании заказа: {e}")
            print(f"Данные клиента: {customer.first_name} {customer.last_name}")
    else:
        print("Выбранный клиент не существует.")




