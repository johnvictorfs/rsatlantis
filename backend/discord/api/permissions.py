from rest_framework.permissions import SAFE_METHODS, BasePermission


class AdminOrReadOnly(BasePermission):
    """
    Allows any safe method for anyone (read-only)

    Allows any method for Admins and Superusers
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser or request.user.is_staff


class IsSuperUser(BasePermission):
    """
    Only allows SuperUsers
    """

    def has_permission(self, request, view):
        return request.user.is_superuser
