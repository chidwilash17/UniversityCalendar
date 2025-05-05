from django.contrib import admin
from .models import  CalendarEvent


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'event_type', 'user_email', 'user', 'created_at')  # Fields in the admin list view
    search_fields = ('title', 'user_email', 'user__username')  # Enable searching by title, email, or username
    list_filter = ('event_type', 'date', 'created_at')  # Add filtering options
    ordering = ('-date',)  # Order the events by date in descending order