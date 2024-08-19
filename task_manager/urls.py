# task_manager/tasks/urls.py
from django.urls import path
from .views import home, TaskCreateView, TaskListView, TaskStatsView, SubTaskCreateView, SubTaskListView

urlpatterns = [
    path('', home, name='home'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/list/', TaskListView.as_view(), name='task-list'),
    path('task/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtask/create/', SubTaskCreateView.as_view(), name='subtask-create'),
    path('subtask/list/', SubTaskListView.as_view(), name='subtask-list'),
]