from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    Everyone can create a new User.
    Everyone can read details of a User. (safe methods)
    Only admins and the actual user can edit a User.
    Only admins can delete a User.
    """

    def has_permission(self, request, view):
        if view.action == 'list':
            # Only allow admin users to see list of users
            return request.user.is_authenticated and request.user.is_staff

        # Allow anyone to create new users
        elif view.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (read-only) for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow admins and the actual user to edit its user account
        elif view.action in ['update', 'partial_update', 'retrieve']:
            return obj == request.user or request.user.is_staff
        # Only allow admins to destroy an account
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False
