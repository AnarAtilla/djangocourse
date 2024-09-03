from rest_framework import viewsets
from .models import Task, SubTask, Category
from .serializers import (
    TaskManagerTaskSerializer, TaskManagerTaskDetailSerializer, TaskManagerSubTaskSerializer,
    TaskManagerCategorySerializer
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .filters import TaskFilter
from rest_framework.views import APIView
from django.db.models import Count
from django.utils import timezone
from django.shortcuts import render

class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskManagerTaskSerializer
    filterset_class = TaskFilter
    ordering_fields = ['deadline', 'created_at']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskManagerTaskDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        tasks = Task.objects.filter(owner=request.user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

class SubTaskViewSet(BaseViewSet):
    queryset = SubTask.objects.all()
    serializer_class = TaskManagerSubTaskSerializer
    filter_fields = ['status', 'deadline']
    ordering_fields = ['deadline', 'created_at']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
    queryset = Category.objects.all().order_by('id')
    serializer_class = TaskManagerCategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(categories=category).count()
        return Response({'task_count': task_count})

def home(request):
    return render(request, 'task_manager/home.html')