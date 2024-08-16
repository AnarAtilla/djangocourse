# project_tasks/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ProjectTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_tasks'

    def ready(self):
        from .signals import assign_permissions
        post_migrate.connect(assign_permissions, sender=self)