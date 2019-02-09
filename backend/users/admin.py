from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class AppUserAdmin(UserAdmin):
    model = User

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return self.request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return self.request.user.is_superuser


admin.site.register(User, AppUserAdmin)
