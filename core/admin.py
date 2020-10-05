from django.contrib import admin
from .models import User, Column, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
admin.site.register(Column)


admin.site.register(Post)
admin.site.register(Comment)