from rest_framework import permissions


class GuidePermission(permissions.BasePermission):
    """
    Only authenticated and active users can create a Guide.
    Only admins and the author of a Guide can update or delete it.
    """
    def has_permission(self, request, view):
        # Allow everyone to get the list of guides
        if view.action == 'list':
            return True
        # Only allow logged in users to create a guide
        elif view.action == 'create':
            return request.user.is_authenticated and request.user.is_active
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Allow anyone to get a guide, but to update/delete one, user needs to be authenticated
        if view.action == 'retrieve':
            return True
        elif not request.user.is_authenticated and request.user.is_active:
            return False
        # Allow admins and the creator of guides to edit or delete a guide
        elif view.action in ['update', 'partial_update']:
            return obj.author == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return obj.author == request.user or request.user.is_staff
        else:
            return False
