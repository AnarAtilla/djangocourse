from rest_framework import serializers
from .models import Event, Task, Project, Tag, ProjectFile

class ProjectTasksEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ProjectTasksTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectTasksProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectTasksTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectTasksProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = '__all__'