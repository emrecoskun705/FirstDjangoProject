from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from .models import Column, User, Post, Comment
from .forms import ColumnForm, PostForm, CommentForm
import datetime

class HomePageView(ListView):
    context_object_name = 'column_list'
    queryset = Column.objects.all()
    template_name='home.html'


class ColumnFormView(FormView):
    template_name = 'column_form.html'
    form_class = ColumnForm
    success_url = '/'

    def form_valid(self, form):
        column = form.save(commit=False)
        column.coordinator = self.request.user
        column.save()
        
        return super().form_valid(column)
        

@login_required
def post_create_in_column(request, column_id):
    form = PostForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        column = get_object_or_404(Column, id=column_id)
        column.posts.add(post)
        column.save()
        return redirect('home')
    return render(request, 'post_form.html', context)


@login_required
def account_profile(request, id):
    user = get_object_or_404(User, id=id)
    columns = Column.objects.filter(coordinator=user)
    posts = Post.objects.filter(author=user)
    
    context = {
        'user': user,
        'columns': columns,
        'posts': posts
    }
    if user:
        return render(request, 'account/profile.html', context)
    else:
        return redirect('home')

def column_list(request, id):
    user = get_object_or_404(User, id=id)
    columns = get_list_or_404(Column, coordinator=user)

    context = {
        'columns': columns
    }

    return render(request, 'column_list.html', context)

def post_list(request, column_id):
    column = get_object_or_404(Column, id=column_id)
    now = datetime.datetime.now()

    context = {
        'column': column,
        'now': now,
    }

    return render(request, 'post_list.html', context)

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(post=post)
    if form.is_valid():
        instance = form.save(commit=False)
        
        instance.author = request.user
        
        instance.post = post
        instance.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, 'post_detail.html', context)

@login_required
def subscribe(request, column_id):
   column = get_object_or_404(Column, id=column_id)
   column.subscribers.add(request.user)
   column.save()
   return redirect('home')

def post_list_for_user(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author=user)

    context = {
        'posts': posts
    }

    return render(request, 'post_list_for_user.html', context)



    