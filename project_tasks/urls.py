# project_tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', views.TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
    path('projectfiles/', views.ProjectFileListCreateView.as_view(), name='projectfile-list-create'),
    path('projectfiles/<int:pk>/', views.ProjectFileRetrieveUpdateDestroyView.as_view(), name='projectfile-detail'),
    path('home/', views.home, name='home'),
]