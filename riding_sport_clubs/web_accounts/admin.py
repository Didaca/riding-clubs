from django.contrib import admin
from django.contrib.auth.models import Group

from riding_sport_clubs.web_accounts.forms import GroupForm
from riding_sport_clubs.web_accounts.models import SiteUser


# @admin.register(SiteUser)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'id',)


@admin.register(SiteUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email',)
    ordering = ('first_name', 'last_name', 'email',)


admin.site.unregister(Group)


class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    filter_horizontal = ['permissions']


admin.site.register(Group, GroupAdmin)
