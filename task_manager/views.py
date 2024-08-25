from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Task, SubTask
from .serializers import TaskSerializer, TaskDetailSerializer, SubTaskSerializer, SubTaskCreateSerializer
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render
from .filters import TaskFilter

def home(request):
    return render(request, 'task_manager/home.html')

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filterset_class = TaskFilter  # Use the filter
    ordering_fields = ['deadline', 'created_at']
    pagination_class = PageNumberPagination

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


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

# SubTask Views
class SubTaskCreateView(generics.CreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

class SubTaskListView(generics.ListAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['status', 'deadline']  # Filter by status and deadline
    ordering_fields = ['deadline', 'created_at']
    pagination_class = PageNumberPagination

class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
