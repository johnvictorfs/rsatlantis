from rest_framework import permissions


class GuidePermission(permissions.BasePermission):
    """
    Only authenticated and active users can create a Guide.
    Only admins and the author of a Guide can update or delete it.
    """

    def has_permission(self, request, view):
        """Anyone can get any guide or list them (safe methods), but only logged in users can create a guide"""
        if view.action == 'create':
            return request.user.is_authenticated and request.user.is_active
        elif view.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Allow anyone to get a guide, but to update/delete one, user needs to be authenticated, and either be
        an admin or the author of said guide
        """
        is_safe = request.method in permissions.SAFE_METHODS
        is_author = request.user == obj.author
        return is_safe or is_author or request.user.is_superuser
