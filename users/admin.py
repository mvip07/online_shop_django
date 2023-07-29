from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin (UserAdmin):
    add_form = RegisterForm
    form = RegisterForm
    model = CustomUser

    list_display = ['email', 'username', 'first_name', 'last_name', 'image', 'phone', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)