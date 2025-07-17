from django.db import models

class CLIENT(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('Individual Client', 'Individual Client'),
        ('Business Client', 'Business Client'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)

    def __str__(self):
        return self.name
