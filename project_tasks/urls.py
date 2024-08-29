from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TaskViewSet, ProjectViewSet, TagViewSet, ProjectFileViewSet, home

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'projectfiles', ProjectFileViewSet, basename='projectfile')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='project_tasks-home'),
]