from rest_framework import viewsets
from .models import Event, Task, Project, Tag, ProjectFile
from .serializers import (
    ProjectTasksEventSerializer, ProjectTasksTaskSerializer, ProjectTasksProjectSerializer,
    ProjectTasksTagSerializer, ProjectTasksProjectFileSerializer
)
from django.shortcuts import render

class BaseViewSet(viewsets.ModelViewSet):
    pass

class EventViewSet(BaseViewSet):
    queryset = Event.objects.all()
    serializer_class = ProjectTasksEventSerializer

class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = ProjectTasksTaskSerializer

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTasksProjectSerializer

class TagViewSet(BaseViewSet):
    queryset = Tag.objects.all()
    serializer_class = ProjectTasksTagSerializer

class ProjectFileViewSet(BaseViewSet):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectTasksProjectFileSerializer

def home(request):
    return render(request, 'project_tasks/home.html')