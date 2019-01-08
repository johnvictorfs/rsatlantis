from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    Everyone can create a new User.
    Only admins and the actual user can retrieve or edit a User.
    Only admins can delete a User.
    """
    def has_permission(self, request, view):
        if view.action == 'list':
            # Only allow admin users to see list of users
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            # Allow anyone to create new users
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        # Allow admins and the actual user to edit its user account
        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        # Only allow admins to destroy an account
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False