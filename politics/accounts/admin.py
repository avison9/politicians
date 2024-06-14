from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

usr = get_user_model()

# Remove Group Model from admin.Not needed.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    update_form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username', 'email', 'admin', 'staff', 'active']
    list_filter = ['admin','staff','active']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('admin','staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password', 'password_2','admin','staff',)}
        ),
    )
    search_fields = ['username']
    ordering = ['email']
    filter_horizontal = ()



admin.site.register(usr, UserAdmin)

