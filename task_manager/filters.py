# task_manager/tasks/filters.py
import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'title': ['exact', 'icontains'],
            'status': ['exact'],
            'priority': ['exact', 'gte', 'lte'],
            'deadline': ['exact', 'gte', 'lte'],
        }