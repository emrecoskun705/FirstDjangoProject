from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save

class User(AbstractUser):
    pass


class Article(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.heading


