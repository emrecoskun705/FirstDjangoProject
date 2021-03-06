from django import forms
from .models import Column, Post, Comment

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ('title',)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('heading', 'content', 'image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content',)

CHOICES = (
    ('moderator', 'Moderator'),
    ('writer', 'Writer')
)

class WorkerForm(forms.Form):
    username = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=CHOICES , widget=forms.RadioSelect, required=True)
