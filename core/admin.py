from django.contrib import admin
from .models import User,Column,Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(Column)
admin.site.register(Post)