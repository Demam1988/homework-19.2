from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'pk', 'is_superuser', 'is_active',)
    list_filter = ('email', 'is_active')

