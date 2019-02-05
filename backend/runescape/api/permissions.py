from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """
    Allows any safe method for anyone (read-only)
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
