from django import forms
from .models import Column, Post, Comment

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('title', 'posts', 'workers', 'subscribers')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content',)
