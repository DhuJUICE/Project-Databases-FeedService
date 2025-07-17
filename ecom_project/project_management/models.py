from django.db import models
from client_management.models import CLIENT

class PROJECT(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    client = models.ForeignKey(CLIENT, on_delete=models.CASCADE, related_name='projects')  # 👈 Add this line
    name = models.CharField(max_length=200)
    description = models.TextField()
    completion_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    to_do = models.JSONField(default=list, blank=True)
    in_progress = models.JSONField(default=list, blank=True)
    completed = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

