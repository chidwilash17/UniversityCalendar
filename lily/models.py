from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class CalendarEvent(models.Model):
    EVENT_TYPE_CHOICES = [
        ('holiday', 'Holiday'),
        ('exam', 'Exam'),
        ('lecture', 'Lecture'),
        ('other', 'Other')
    ]
    
    title = models.CharField(max_length=200)
    date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    description = models.TextField(blank=True)
    user_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} ({self.date})"
    
    def get_event_type_display(self):
        return dict(self.EVENT_TYPE_CHOICES).get(self.event_type, 'Other')