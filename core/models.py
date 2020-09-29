from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save

class User(AbstractUser):
    
    #coordinators can create columns
    coordinator = models.BooleanField(default=False)


class Column(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post')
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    workers = models.ManyToManyField(User, related_name='workers')
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    class Meta:
        permissions = (
            ('create_post', 'Create Post'),
            ('approve_post', 'Approve Post')
        )

    def __str__(self):
        return self.title


class Post(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.heading


