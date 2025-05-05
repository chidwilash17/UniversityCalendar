# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from .models import CalendarEvent

@shared_task
def send_event_reminders():
    tomorrow = timezone.now().date() + timedelta(days=1)
    events = CalendarEvent.objects.filter(date=tomorrow)
    
    for event in events:
        send_mail(
            f'Reminder: {event.title}',
            f'''Your event "{event.title}" is scheduled for tomorrow.\n\nDescription: {event.description}''',
            settings.DEFAULT_FROM_EMAIL,
            [event.user.email],
            fail_silently=False,
        )