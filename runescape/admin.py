from django.contrib import admin
from runescape.models import ClanMember


class ClanMemberAdmin(admin.ModelAdmin):
    model = ClanMember
    readonly_fields = ('name', 'exp', 'rank')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ClanMember, ClanMemberAdmin)
