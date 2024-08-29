from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import TaskFilter
from .models import Category, Task
from .models import SubTask
from .serializers import TaskManagerCategorySerializer
from .serializers import (
    TaskManagerTaskSerializer, TaskManagerTaskDetailSerializer, TaskManagerSubTaskSerializer
)


def home(request):
    return render(request, 'task_manager/home.html')

class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskManagerTaskSerializer
    filterset_class = TaskFilter
    ordering_fields = ['deadline', 'created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskManagerTaskDetailSerializer
        return super().get_serializer_class()

class SubTaskViewSet(BaseViewSet):
    queryset = SubTask.objects.all()
    serializer_class = TaskManagerSubTaskSerializer
    filter_fields = ['status', 'deadline']
    ordering_fields = ['deadline', 'created_at']

class TaskStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        return Response({
            'total_tasks': total_tasks,
            'status_counts': status_counts,
            'overdue_tasks': overdue_tasks,
        })

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')  # Добавлен порядок сортировки
    serializer_class = TaskManagerCategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(categories=category).count()
        return Response({'task_count': task_count})