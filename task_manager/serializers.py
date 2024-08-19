# task_manager/tasks/serializers.py
from rest_framework import serializers
from .models import Task, Category, SubTask

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'categories']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        task = Task.objects.create(**validated_data)
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            task.categories.add(category)
        return task

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'priority', 'deadline', 'task']

    def create(self, validated_data):
        subtask = SubTask.objects.create(**validated_data)
        return subtask