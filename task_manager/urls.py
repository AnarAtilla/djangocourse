from django.urls import path
from .views import home, TaskCreateView, TaskListView, TaskDetailView, TaskStatsView, SubTaskCreateView, SubTaskListView, SubTaskDetailView

urlpatterns = [
    path('', home, name='home'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/list/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtask/create/', SubTaskCreateView.as_view(), name='subtask-create'),
    path('subtask/list/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtask/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
]