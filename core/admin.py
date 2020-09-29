from django.contrib import admin
from .models import User,Column,Post

admin.site.register(User)
admin.site.register(Column)
admin.site.register(Post)