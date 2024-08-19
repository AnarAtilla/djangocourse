# task_manager/tasks/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer, SubTaskCreateSerializer
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from .filters import TaskFilter  # Импортируйте фильтр

def home(request):
    return render(request, 'task_manager/home.html')

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TaskFilter  # Используйте фильтр
    ordering_fields = ['deadline', 'created_at']
    pagination_class = PageNumberPagination

class TaskStatsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        return Response({
            'total_tasks': total_tasks,
            'status_counts': status_counts,
            'overdue_tasks': overdue_tasks,
        })

class SubTaskCreateView(generics.CreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

class SubTaskListView(generics.ListAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['deadline', 'created_at']
    pagination_class = PageNumberPagination