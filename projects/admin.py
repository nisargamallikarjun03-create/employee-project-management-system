from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'client_name',
        'project_manager',
        'status',
        'start_date',
        'end_date',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'project_name',
        'client_name',
    )