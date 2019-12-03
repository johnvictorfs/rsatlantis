from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrReadOnly(BasePermission):
    """
    Allows any safe method for anyone (read-only)

    Allows any method for Admins and Superusers
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser or request.user.is_staff
