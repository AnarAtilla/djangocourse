# project_tasks/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_migrate)
def assign_permissions(sender, **kwargs):
    # Step 1: Create groups
    manager_group, created = Group.objects.get_or_create(name='Manager')
    client_group, created = Group.objects.get_or_create(name='Client')
    developer_group, created = Group.objects.get_or_create(name='Developer')

    # Step 2: Define permissions
    permissions = {
        'Manager': [
            'auth.view_group', 'auth.view_permission', 'auth.add_permission', 'auth.add_user', 'auth.view_user',
            'project_tasks.add_project', 'project_tasks.change_project', 'project_tasks.delete_project', 'project_tasks.view_project',
            'project_tasks.add_projectfile', 'project_tasks.change_projectfile', 'project_tasks.delete_projectfile', 'project_tasks.view_projectfile',
            'project_tasks.add_tag', 'project_tasks.change_tag', 'project_tasks.view_tag',
            'project_tasks.add_task', 'project_tasks.change_task', 'project_tasks.view_task'
        ],
        'Client': [
            'auth.add_user', 'auth.change_user', 'auth.view_user',
            'project_tasks.add_project', 'project_tasks.change_project', 'project_tasks.view_project',
            'project_tasks.add_projectfile', 'project_tasks.view_projectfile',
            'project_tasks.add_tag', 'project_tasks.change_tag', 'project_tasks.delete_tag', 'project_tasks.view_tag',
            'project_tasks.add_task', 'project_tasks.change_task', 'project_tasks.delete_task', 'project_tasks.view_task'
        ],
        'Developer': [
            'auth.add_user', 'auth.change_user', 'auth.delete_user', 'auth.view_user',
            'project_tasks.add_project', 'project_tasks.change_project', 'project_tasks.delete_project', 'project_tasks.view_project',
            'project_tasks.add_projectfile', 'project_tasks.change_projectfile', 'project_tasks.delete_projectfile', 'project_tasks.view_projectfile',
            'project_tasks.add_tag', 'project_tasks.change_tag', 'project_tasks.delete_tag', 'project_tasks.view_tag',
            'project_tasks.add_task', 'project_tasks.change_task', 'project_tasks.delete_task', 'project_tasks.view_task'
        ]
    }

    # Step 3: Assign permissions to groups
    for group_name, perms in permissions.items():
        group = Group.objects.get(name=group_name)
        for perm in perms:
            try:
                app_label, codename = perm.split('.')
                content_type = ContentType.objects.get(app_label=app_label, model=codename.split('_')[1])
                permission = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(permission)
            except (Permission.DoesNotExist, ContentType.DoesNotExist):
                print(f"Permission {perm} does not exist.")