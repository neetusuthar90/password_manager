from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 200)
    date_joined = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
