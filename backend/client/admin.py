from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'name', 'email', 'phone_number', 'country', 'city', 'postal_code')

    # Fields to filter in the admin list view
    list_filter = ('country', 'city', 'customer_tags')

    # Fields to search in the admin list view
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'name')

    # Fields to display in the edit form
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'customer_tags', 'country', 'address', 'city', 'postal_code')

    # Read-only fields
    readonly_fields = ('name',)
