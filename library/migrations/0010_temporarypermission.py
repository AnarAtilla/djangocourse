# Generated by Django 5.0.7 on 2024-08-29 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_author_options_alter_book_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=255, verbose_name='Permission')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temporary_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
