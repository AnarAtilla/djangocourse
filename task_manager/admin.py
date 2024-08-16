from django.contrib import admin

from .models import Category, Task, SubTask


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'deadline', 'created_at')
    list_filter = ('status', 'priority', 'deadline')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'priority', 'deadline', 'created_at')
    list_filter = ('status', 'priority', 'deadline')
    search_fields = ('title', 'description')
