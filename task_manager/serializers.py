from rest_framework import serializers
from .models import Task, Category, SubTask
from django.utils import timezone
from drf_yasg.utils import swagger_serializer_method

class TaskManagerCategorySerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'task_count']

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_task_count(self, obj):
        return Task.objects.filter(categories=obj).count()

class TaskManagerTaskSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'categories', 'owner']
        read_only_fields = ['owner']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        task = Task.objects.create(**validated_data)
        task.categories.set(categories_data)
        return task

class TaskManagerSubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'priority', 'deadline', 'task', 'owner']
        read_only_fields = ['owner']

    def create(self, validated_data):
        subtask = SubTask.objects.create(**validated_data)
        return subtask

class TaskManagerSubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'priority', 'deadline', 'task', 'created_at', 'owner']
        read_only_fields = ['owner']

class TaskManagerCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        name = validated_data['name']
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        if Category.objects.filter(name=name).exclude(id=instance.id).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return super().update(instance, validated_data)

class TaskManagerTaskDetailSerializer(serializers.ModelSerializer):
    subtasks = TaskManagerSubTaskSerializer(many=True, read_only=True)
    categories = TaskManagerCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'categories', 'subtasks', 'owner']
        read_only_fields = ['owner']

class TaskManagerTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'categories', 'owner']
        read_only_fields = ['owner']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value

class TaskStatsSerializer(serializers.Serializer):
    total_tasks = serializers.IntegerField()
    status_counts = serializers.DictField(child=serializers.IntegerField())
    overdue_tasks = serializers.IntegerField()
