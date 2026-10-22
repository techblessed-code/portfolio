from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at', 'read')
    list_filter = ('read',)
    readonly_fields = ('name', 'email', 'subject', 'body', 'created_at')
