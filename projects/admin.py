from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'completed', 'created_at')
    list_filter = ('category', 'featured', 'technologies')
    prepopulated_fields = {'slug': ('title',)}     # slug fills itself from title
    search_fields = ('title', 'summary')
