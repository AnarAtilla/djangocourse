from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date']

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if end_date and start_date and end_date < start_date:
            raise forms.ValidationError('End date cannot be earlier than start date.')
        return end_date

class Task(models.Model):
    STATUSES_CHOICES = [
        ('New', 'New'),
        ('In_progress', 'In_progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Very High', 'Very High'),
    ]

    title = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(10)])
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUSES_CHOICES, default='New', max_length=15)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=15)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    files = models.ManyToManyField('ProjectFile', blank=True, related_name='tasks')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-due_date', 'assignee']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        unique_together = (('title', 'project'),)

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField('ProjectFile', blank=True, related_name='projects')

    @property
    def count_of_files(self):
        return self.files.count()

    def __str__(self):
        return f"Project: {self.title}"

    class Meta:
        ordering = ['-title']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='Projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']