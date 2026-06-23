from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display    = ['name', 'email', 'subject', 'sent_at', 'is_read']
    list_filter     = ['is_read']
    search_fields   = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']