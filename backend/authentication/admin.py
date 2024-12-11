from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'role', 'status', 'created_at', 'updated_at')
    search_fields = ('username', 'name')
    list_filter = ('role', 'status')
    fieldsets = (
        (None, {'fields': ('name', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )
    actions = ['mark_as_inactive']

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='Inactive')
    mark_as_inactive.short_description = "Mark selected users as inactive"