from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

from .forms import UserAdminCreationForm, UserAdminChangeForm

usr = get_user_model()

# Remove Group Model from admin.Not needed.
admin.site.unregister(Group)

#Integrating the profile details into the Users details in the admin panel
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    update_form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username', 'email', 'first_name','last_name','country', 'created_at', 'admin', 'staff', 'active']
    list_filter = ['admin','staff','active']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name','last_name','username','country',)}),
        ('Permissions', {'fields': ('admin','staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','country','email', 'password', 'password_2','admin','staff',)}
        ),
    )
    search_fields = ['username']
    ordering = ['email']
    filter_horizontal = ()

    inlines = (ProfileInline,)




admin.site.register(usr, UserAdmin)
admin.site.register(Profile)

