from django import forms
from .models import Column, Post

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('title', 'posts', 'workers', 'subscribers')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)