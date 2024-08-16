# task_manager/urls.py
from django.urls import path
from .views import home, TaskCreateView, TaskListView, TaskStatsView

urlpatterns = [
    path('', home, name='home'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),
]