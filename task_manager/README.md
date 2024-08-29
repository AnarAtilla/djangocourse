# Task Manager

## Описание

Task Manager - это приложение для управления задачами, которое позволяет создавать, обновлять и отслеживать задачи, подзадачи и категории.

## Модели

### Category (Категория)

- `name`: CharField (max_length=100, unique=True) - название категории.

### Task (Задача)

- `title`: CharField (max_length=200, unique=True) - заголовок задачи.
- `description`: TextField - описание задачи.
- `categories`: ManyToManyField (Category) - категории, к которым относится задача.
- `status`: CharField (max_length=20, choices=STATUS_CHOICES, default='new') - статус задачи.
- `priority`: IntegerField (default=1) - приоритет задачи.
- `deadline`: DateTimeField - крайний срок выполнения задачи.
- `created_at`: DateTimeField (auto_now_add=True) - время создания задачи.

### SubTask (Подзадача)

- `title`: CharField (max_length=200, unique=True) - заголовок подзадачи.
- `description`: TextField - описание подзадачи.
- `task`: ForeignKey (Task, related_name='subtasks', on_delete=models.CASCADE) - задача, к которой относится подзадача.
- `status`: CharField (max_length=20, choices=STATUS_CHOICES, default='new') - статус подзадачи.
- `priority`: IntegerField (default=1) - приоритет подзадачи.
- `deadline`: DateTimeField - крайний срок выполнения подзадачи.
- `created_at`: DateTimeField (auto_now_add=True) - время создания подзадачи.

## Административная панель

Для управления моделями через административную панель Django, зарегистрируйте модели в `admin.py`:

```python
from django.contrib import admin
from .models import Category, Task, SubTask

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'deadline', 'created_at')
    list_filter = ('status', 'priority', 'deadline')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'priority', 'deadline', 'created_at')
    list_filter = ('status', 'priority', 'deadline')
    search_fields = ('title', 'description')

## Установка и запуск
Для установки и запуска приложения выполните следующие шаги:
## 1. Клонирование репозитория
```bash
git clone <URL_репозитория>
cd MyPro


## 2. Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

## 3. Установите зависимости:
pip install -r requirements.txt

## 4. Примените миграции:
python manage.py makemigrations task_manager
python manage.py migrate

## 5. Создайте суперпользователя:
python manage.py createsuperuser

## 6. Запустите сервер:
python manage.py runserver
```

## Использование

После запуска сервера, вы можете получить доступ к приложению по адресу http://127.0.0.1:8000/tasks/.

## Лицензия

Этот проект лицензирован под лицензией MIT.

