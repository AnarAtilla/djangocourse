# Generated by Django 5.0.7 on 2024-08-08 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lagerhouse', '0002_yourmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yourmodel',
            options={'ordering': ['-created_at']},
        ),
    ]
