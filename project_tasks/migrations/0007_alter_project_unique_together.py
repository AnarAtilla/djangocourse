# Generated by Django 5.0.7 on 2024-08-06 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_tasks', '0006_task_files'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set(),
        ),
    ]