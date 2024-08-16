# project_tasks/views.py
from rest_framework import generics
from .models import Event, Task, Project, Tag, ProjectFile
from .serializers import EventSerializer, TaskSerializer, ProjectSerializer, TagSerializer, ProjectFileSerializer
from django.shortcuts import render

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProjectFileListCreateView(generics.ListCreateAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer

class ProjectFileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer

def home(request):
    return render(request, 'project_tasks/home.html')