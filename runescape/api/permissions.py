from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnly(BasePermission):
    """
    Allows any safe method for anyone (read-only)
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
