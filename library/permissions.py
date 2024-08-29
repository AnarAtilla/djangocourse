from rest_framework import permissions
from .models import TemporaryPermission
from django.utils import timezone

class HasTemporaryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        permission = view.get_permission_name()  # Метод, который возвращает имя разрешения для ViewSet
        temp_permissions = TemporaryPermission.objects.filter(
            user=request.user,
            permission=permission,
            start_time__lte=timezone.now(),
            end_time__gte=timezone.now()
        )
        return temp_permissions.exists()