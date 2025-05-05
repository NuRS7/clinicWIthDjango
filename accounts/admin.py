
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'is_patient', 'is_doctor', 'is_staff')
    list_filter = ('is_patient', 'is_doctor', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name')}),
        ('Роли', {'fields': ('is_patient', 'is_doctor')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(User, CustomUserAdmin)
