from django.contrib import admin
from django.contrib import messages
from .models import Tag, Project, Task


def change_status(modeladmin, request, queryset):
    queryset.update(status='Closed')
    modeladmin.message_user(request, "Status changed to Closed in selected tasks.", messages.SUCCESS)


change_status.short_description = 'Mark as Closed'


def set_priority_low(modeladmin, request, queryset):
    queryset.update(priority='Low')


set_priority_low.short_description = 'Set priority to Low'


def set_priority_medium(modeladmin, request, queryset):
    queryset.update(priority='Medium')


set_priority_medium.short_description = 'Set priority to Medium'


def set_priority_high(modeladmin, request, queryset):
    queryset.update(priority='High')


set_priority_high.short_description = 'Set priority to High'


def set_priority_very_high(modeladmin, request, queryset):
    queryset.update(priority='Very High')


set_priority_very_high.short_description = 'Set priority to Very High'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'create_at', 'count_of_files']
    search_fields = ['title', 'description']
    list_filter = ['create_at']

    def count_of_files(self, obj):
        return obj.files.count()

    count_of_files.short_description = 'Count of Files'

    def replace_spaces_with_underscores(self, request, queryset):
        for project in queryset:
            project.title = project.title.replace(' ', '_')
            project.save()
        self.message_user(request, "Spaces replaced with underscores in selected projects.", messages.SUCCESS)

    replace_spaces_with_underscores.short_description = 'Replace spaces with underscores in titles'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'created_at', 'due_date', 'assignee']
    search_fields = ['title']
    list_filter = ['status', 'priority', 'project', 'created_at', 'due_date', 'assignee']
    date_hierarchy = 'created_at'
    actions = [change_status, set_priority_low, set_priority_medium, set_priority_high, set_priority_very_high]
