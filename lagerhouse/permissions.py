from rest_framework import permissions

class IsCustomerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow customers to edit their own data.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.customer == request.user.customer

class CanViewStatistics(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_statistics' permission.
    """

    def has_permission(self, request, view):
        return request.user.has_perm('lagerhouse.can_view_statistics')