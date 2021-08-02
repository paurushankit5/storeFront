import datetime
from django.db import models
from django.utils import timezone



class ServerDetails(models.Model):
    server_name = models.CharField(max_length=200)
    details = models.TextField()
    def __str__(self):
        return self.server_name